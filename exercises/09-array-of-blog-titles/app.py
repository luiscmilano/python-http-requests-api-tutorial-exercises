import requests

def get_titles():
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php').json()
    titles = []

    for title in response['posts']:
        titles.append(title['title'])

    return titles


print(get_titles())