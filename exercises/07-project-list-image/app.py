import requests

# your code here
response = requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php').json()

print(response[-1]['images'][-1])