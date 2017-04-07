import requests
url = 'http://0.0.0.0:8000/'
files = {'file': open('einstein.jpg', 'rb')}
requests.post(url, files=files)
print open('einstein.jpg', 'rb')
