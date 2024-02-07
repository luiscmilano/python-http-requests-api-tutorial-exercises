import requests

def get_post_tags(post_id):
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php').json()

    tags = []

    for tag in response['posts']:
        if tag['id'] == post_id:
            tags.append(tag['tags'])

    return tags


print(get_post_tags(146))