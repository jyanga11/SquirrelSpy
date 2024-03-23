import requests
import datetime

base_url = "http://localhost:8000"
endpoint = "/sightings/"

img_file_path = "/Users/jyanga/Downloads/unnamed (1).jpg"

data = {
            'user': 2,
            'squirrel': 2,
            'lat': -2.342,
            'long': 11.985,
            'time': datetime.datetime.now(),
            'behavior': 'Sleeping',
            'certainty_level': 4
       }

with open(img_file_path, 'rb') as file:
    files = {'image': file}
    response = requests.post(base_url + endpoint, data=data, files=files)

print(response.status_code)
print(response.text)