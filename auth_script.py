from passwords import username, password
import requests

response = requests.get(f'http://localhost/basic-auth/{username}/{password}', auth=(username, password))
print(response.json())
