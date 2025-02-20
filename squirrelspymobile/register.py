import requests

base_url = "http://localhost:8000"
endpoint = "/register/"

img_file_path = "/Users/jyanga/Downloads/IMG_4036.jpg"

data = {
            'username': 'user1',
            'email': 'user1@coe.edu',
            'password': 'password1'
       }

with open(img_file_path, 'rb') as file:
    files = {'image': file}
    response = requests.post(base_url + endpoint, data=data, files=files)

print(response.status_code)
print(response.text)