from data_preprocessing import preprocess_data
from data_aquisition import fetch_repository_data
from sql_db import *
from analyze_data import draw_data_grpahs

#github repository data aquisition through github web api
#need to pass valid pat token here
repository_data = fetch_repository_data("pat_token")
#preprocess the data to filter out required data
preprocessed_data = preprocess_data(repository_data)
#store the data into a sql database
db_name = '../db/github_data.db'
create_database(db_name)
load_data_to_database(preprocessed_data, db_name)
#analyze the data
draw_data_grpahs(db_name)
