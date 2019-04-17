Completed: 16-Apr-2019

# Project: Data Modeling with Postgres
Model data with Postgres and build an ETL pipeline using Python.
 - define fact and dimension tables for a star schema for a particular analytic focus
 - write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# Available Data Sets - Song and Log
Under a data folder, 2 kinds of datasets were provided. Both the datasets contained files in JSON format, in a folder structure.

# Helpful Templates
The following jupyter notebooks were easy to use templates to build the project step-by-step - 
1. "test.ipynb" displays the first few rows of each table to let you check your database.
2. "etl.ipynb" reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
Note: These Notebooks are a good help to build the project but are not required. So these are not available under this repository.

# Setup Instructions
For this project, I used the Udacity workspace even though I set up Postgres and Jupyter Notebook to run locally while following the lessons.

There was no set-up required while using the Udacity workspace, but I made sure that I imported all the relevant libraries, set up appropriate connections to the database and restart kernels at the right time. Performing these steps at the right times was important while working through the commands in etl.ipynb

I have used etl.ipynb to come up with the commands to read data. As I was working through this file, I updated sql_queries.py for relevant queries. As I completed each of the 5 steps in etl.ipynb, I tested them using test.ipynb. 

Once all the steps in etl.ipynb were completed successfully, I completed etl.py for processing the data sets.

# Schema Design
 - Fact Table
     - "songplays" - records in log data associated with song plays i.e. records with page NextSong
         - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
 - Dimension Tables
     - "users" - users in the app
         - user_id, first_name, last_name, gender, level
     - "songs" - songs in music database
         - song_id, title, artist_id, year, duration
     - "artists" - artists in music database
         - artist_id, name, location, lattitude, longitude
     - "time" - timestamps of records in songplays broken down into specific units
         - start_time, hour, day, week, month, year, weekday

# Program execution
1. To run this program locally or in the workspace, make sure that the data folder, sql_queries.py, create_tables.py, and etl.py must all be available under the same folder.
2. Open the terminal window and navigate to where all the folders and files from step 1 are located.
3. Execute the following commands in order - 
     - python3 create_tables.py
     - python3 etl.py
    
# Testing the program
1. Ideally, also place the test.ipynb in the same folder where you have stored the program execution files.
2. Run each command in the test.ipynb to test your program.
3. We can choose to create our own test queries and run them inside the test notebook.

# Reference
1. All the links provided in Udacity lessons.
2. Googled python commands.
3. Learn't using Pandas by going through Slack project-1-dend-v1 channel, mentor help, and https://www.dataquest.io/blog/python-json-tutorial/
