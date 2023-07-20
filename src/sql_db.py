import sqlite3
import pandas as pd
import os

def create_database(db_name):
    if os.path.exists(db_name):
        # if the database file already exists, then remove it.
        os.remove(db_name)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE repositories
                 (name TEXT, language TEXT, stars INTEGER)''')
    conn.commit()
    conn.close()

def load_data_to_database(data, db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # check if the table 'repositories' exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='repositories'")
    table_exists = c.fetchone()

    if not table_exists:
        # create it
        c.execute('''CREATE TABLE repositories
                     (name TEXT, language TEXT, stars INTEGER)''')
        conn.commit()

    # filter out rows with None values in the 'language' column
    data_filtered = data.dropna(subset=['language'])
    # insert filtered data into the 'repositories' table
    c.executemany('INSERT INTO repositories VALUES (?, ?, ?)', data_filtered.values.tolist())
    conn.commit()
    conn.close()


def read_data_from_database(db_name):
    conn = sqlite3.connect(db_name)
    query = 'SELECT language, COUNT(*) AS repository_count, AVG(stars) AS avg_stars FROM repositories GROUP BY language'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df