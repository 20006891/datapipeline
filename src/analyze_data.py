import pandas as pd
import matplotlib.pyplot as plt
from sql_db import read_data_from_database

def draw_data_grpahs(db_name):
    df = read_data_from_database(db_name)   
    # plotting the number of repositories per language
    plt.figure(figsize=(12, 6))
    plt.bar(df['language'], df['repository_count'])
    plt.xlabel('programming language')
    plt.ylabel('repository count')
    plt.title('number of repositories per Language')
    plt.xticks(rotation=90)
    plt.show()

    # plotting the distribution of star counts per language
    plt.figure(figsize=(12, 6))
    plt.boxplot([df[df['language'] == lang]['avg_stars'] for lang in df['language']])
    plt.xlabel('programming Language')
    plt.ylabel('star count')
    plt.title('distribution of star counts per language')
    plt.xticks(range(1, len(df['language']) + 1), df['language'], rotation=90)
    plt.show()

