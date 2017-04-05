import requests
url = 'http://0.0.0.0:8000/'
files = {'file': open('cgresult.png', 'rb')}
requests.post(url, files=files)
