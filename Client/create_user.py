import requests

base_url = "http://localhost:8000"
endpoint = "/users/"

img_file_path = "/Users/jyanga/Downloads/IMG_4036.jpg"

data = {
            'username': 'dhughes',
            'email': 'dhughes21@coe.edu',
            'password': 'mypassword'
       }

with open(img_file_path, 'rb') as file:
    files = {'image': file}
    response = requests.post(base_url + endpoint, data=data, files=files)

print(response.status_code)
print(response.text)