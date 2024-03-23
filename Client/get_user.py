import requests

base_url = "http://localhost:8000"
endpoint = "/users/2/"

data = {}

response = requests.get(base_url + endpoint, data=data)

print(response.status_code)
print(response.text)