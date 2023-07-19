
import requests

#Aquiring/gathering data through web scrapping
def fetch_repository_data(token):
    headers = {
        'Authorization': f'Token {token}'
    }
    url = 'https://api.github.com/search/repositories?q=stars:>0&per_page=100'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to fetch repository data')

# Call the function with GitHub access token
repository_data = fetch_repository_data('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')
print(repository_data)