#GET REQUEST.

import requests
import base64

def request(url, username, password):
    credentials = f'{username}:{password}'.encode('utf-8')
    auth_header = f'Basic {base64.b64encode(credentials).decode()}'
    headers = {'Authorization': auth_header}
    response = requests.get(url, headers=headers)
    return response.text

url = ''
username = ''
password = ''

response = request(url, username, password)
print(response)
