import requests

#aquiring/gathering data through web scrapping
def fetch_repository_data(token):
    headers = {
        'Authorization': f'Token {token}'
    }
    url = 'https://api.github.com/search/repositories?q=stars:>0&per_page=100'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        raise Exception('Failed to fetch repository data')
