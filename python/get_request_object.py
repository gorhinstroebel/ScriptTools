import requests
import base64

# Object Orianted Approach
class API:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.auth_header = f'Basic {base64.b64encode(f"{self.username}:{self.password}".encode()).decode()}'

    def request(self):
        headers = {'Authorization': self.auth_header}
        response = requests.get(self.url, headers=headers)
        return response.text

# Usage example
api = API('url', 'username', 'password')
response = api.request()
print(response)
