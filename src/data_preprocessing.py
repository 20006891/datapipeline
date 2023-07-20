import pandas as pd
from data_aquisition import fetch_repository_data

#pre processing the data
def preprocess_data(repository_data):
    repositories = repository_data['items']
    extracted_data = []
    for repo in repositories:
        extracted_data.append({
            'name': repo['name'],
            'language': repo['language'],
            'stars': repo['stargazers_count']
        })
    df = pd.DataFrame(extracted_data)
    return df
