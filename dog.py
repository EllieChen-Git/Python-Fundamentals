import requests

api_url = "http://shibe.online/api/shibes?count=1"

params = {"count": 10} # Create params as dictionary
response = requests.get(api_url, params=params) # pass 'params' to url

status_code = response.status_code
print("status code:", status_code)
print(response.json())