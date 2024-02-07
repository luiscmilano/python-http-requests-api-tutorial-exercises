import requests

def get_attachment_by_id(attachment_id):
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php').json()
    attachment = {}

    for i in response['posts']:
        if len(i['attachments']) > 0:
            for j in i['attachments']:
                if j['id'] == attachment_id:
                    attachment = j

    return attachment

print(get_attachment_by_id(137))