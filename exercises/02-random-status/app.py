import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")
import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

if response.status_code == 404:
    print('The URL you asked is not found')
if response.status_code == 503:
    print('Unavailable right now')
if response.status_code == 200:
    print('Everything went perfect')
if response.status_code == 400:
    print('Something is wrong on the request params')
else:
    print('anything')