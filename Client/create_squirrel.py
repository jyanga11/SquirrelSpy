import requests

base_url = "http://localhost:8000"
endpoint = "/squirrels/"

img_file_path = "/Users/jyanga/Downloads/unnamed (1).jpg"

data = {
            'name': 'squeakster',
            'weight': 13,
            'sex': 'M',
            'age': 3,
            'species': 'Brown',
            'serial_num': 'X3G78B2',
            'left_ear_color': 'green',
            'right_ear_color': 'blue'
       }

with open(img_file_path, 'rb') as file:
    files = {'image': file}
    response = requests.post(base_url + endpoint, data=data, files=files)

print(response.status_code)
print(response.text)