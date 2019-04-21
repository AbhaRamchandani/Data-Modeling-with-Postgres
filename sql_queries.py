# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
 (songplay_id SERIAL PRIMARY KEY,
 start_time TIME NOT NULL,
 user_id int NOT NULL,
 level text,
 song_id text,
 artist_id text,
 session_id int,
 location text,
 user_agent text);
 """)

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
 (user_id int PRIMARY KEY,
 first_name text,
 last_name text,
 gender char,
 level text);
 """)

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
 (song_id text PRIMARY KEY,
 title text,
 artist_id text,
 year int,
 duration real);
 """)

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
 (artist_id text PRIMARY KEY,
 name text,
 location text,
 lattitude real,
 longitude real);
 """)

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
 (start_time TIME PRIMARY KEY,
 hour int,
 day int,
 week int,
 month int,
 year int,
 weekday int);
 """)

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
(start_time, user_id, level, song_id, artist_id, session_id,
location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users
(user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO
UPDATE SET
first_name=users.first_name,
last_name=users.last_name,
gender=users.gender,
level=users.level;
""")

song_table_insert = ("""
INSERT INTO songs
(song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO
UPDATE SET
title=songs.title, 
artist_id=songs.artist_id,
year=songs.year,
duration=songs.duration;
""")

artist_table_insert = ("""
INSERT INTO artists
(artist_id, name, location, lattitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO
UPDATE SET
name=artists.name,
location=artists.location,
lattitude=artists.lattitude,
longitude=artists.longitude;
""")

time_table_insert = ("""
INSERT INTO time
(start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO
UPDATE SET
hour=time.hour,
day=time.day,
week=time.week,
month=time.month, 
year=time.year,
weekday=time.weekday;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id, s.duration
FROM songs s
LEFT OUTER JOIN artists as a
on a.artist_id =  s.artist_id
WHERE s.title =%s and a.name =%s and s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop]
