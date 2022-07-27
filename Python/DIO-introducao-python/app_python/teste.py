import requests
url = 'https://digitalinnovation.one'
response = requests.get(url)
status_code = response.status_code
print(status_code)