'''This python fies is used to traverse and process all the files
under the data folder. The processed data is inserted into the tables
in the Sparify database.'''


import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


'''Method to process all the song files inside the 'data' folder.
This method reads each file and inserts data in the Sparkify tables.
This method is called from main -> process_data.
The method is designed to process each song file, which is in JSON format.
The looping logic to traverse each file is handled inside process_data.'''


def process_song_file(cur, filepath):
    # open song file - defined df
    df = pd.read_json(filepath, lines=True)

    # insert song record - defined song_cols and song_data
    song_cols = ["song_id", "title", "artist_id", "year", "duration"]
    song_data = df[song_cols].values[0].tolist()
    cur.execute(song_table_insert, song_data)

    # insert artist record - defined artist_cols and artist_data
    artist_cols = [
        "artist_id",
        "artist_name",
        "artist_location",
        "artist_latitude",
        "artist_longitude"]
    artist_data = df[artist_cols].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


'''Method to process all the log files inside the 'data' folder.
This method reads each file and inserts data in the Sparkify tables.
This method is called from main -> process_data.
The method is designed to process each log file, which is in JSON format.
The looping logic to traverse each file is handled inside process_data.'''


def process_log_file(cur, filepath):
    # open log file - defined df
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action - defined df
    df = df.loc[df['page'] == 'NextSong']

    # convert timestamp column to datetime - defined t
    t = pd.to_datetime(df['ts'], unit='ms')

    # insert time data records - defined
    # time_data, column_labels, time_dict, time_df
    time_data = (t, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_dict = dict(zip(column_labels, time_data))
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table - defined user_df
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


'''This method loops through all the song and log files and calls
process_song_file and process_log_file appropriately.'''


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory and its subdirectories
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


'''Set up connection and call process_data method for processing files.'''


def main():
    '''Connect to the Database, Sparkify.'''
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    '''Function calls to gather (in a list) and
    process all of song and log data files.'''
    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()

'''The program starts here!!!'''
if __name__ == "__main__":
    main()
