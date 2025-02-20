import requests

base_url = "http://localhost:8000"
endpoint = "/login/"

data = {
            'username': 'user1',
            'password': 'password1'
       }

response = requests.post(base_url + endpoint, data=data)

print(response.status_code)
print(response.text)