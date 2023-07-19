import pandas as pd
from data_aquisition import fetch_repository_data
#Pre processing the data
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


# Preprocess the repository data
preprocessed_data = preprocess_data(fetch_repository_data('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'))
print(preprocessed_data)
