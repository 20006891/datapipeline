import sqlite3
import pandas as pd

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE repositories
                 (name TEXT, language TEXT, stars INTEGER)''')
    conn.commit()
    conn.close()

def load_data_to_database(data, db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.executemany('INSERT INTO repositories VALUES (?, ?, ?)', data.values.tolist())
    conn.commit()
    conn.close()


def read_data_from_database(db_name):
    conn = sqlite3.connect(db_name)
    query = 'SELECT language, COUNT(*) AS repository_count, AVG(stars) AS avg_stars FROM repositories GROUP BY language'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
    
# Create the database and load data
#create_database('../db/github_data.db')
#load_data_to_database(preprocessed_data, 'github.db')