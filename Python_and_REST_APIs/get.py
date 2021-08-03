import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(f'JSON: {response.json()}')
print(f'Status Code: {response.status_code}')
print(f'Headers: {response.headers["Content-Type"]}')
