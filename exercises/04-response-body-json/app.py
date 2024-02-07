import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
jason = response.json()
print(f'Current time: {jason["hours"]} hrs {jason["minutes"]} min and {jason["seconds"]} sec')