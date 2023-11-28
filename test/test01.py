import requests
import os
url = "http://localhost:9000/api/barcode/"

payload = {}

fis = os.listdir('static')
files = list(map(lambda x: ('file',(f'{x}',open(f'static/{x}','rb'),f'image/jpeg')), fis))
print(files)
# files=[
#   ('file',('a0b31b02b3401a1e4351.jpg',open('static/a0b31b02b3401a1e4351.jpg','rb'),'image/jpeg'))
# ]
for file in files:

    headers = {
        'accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=[file])

    print(response.text)
