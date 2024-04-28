import requests

payload = {'username':'parasverma', 'password':'ayushparas'}
url = 'http://localhost:8000/gettoken/'

response = requests.post(url, json=payload)

print(response.content)