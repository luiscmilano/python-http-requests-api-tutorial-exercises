import requests

myobj = {'somekey': 'somevalue'}

response = requests.post('https://assets.breatheco.de/apis/fake/sample/post.php', json = myobj)

print(response.text)