import requests

response = requests.get('https://assets.breatheco.de/apis/fake/sample/hello.php')

print(response.status_code)