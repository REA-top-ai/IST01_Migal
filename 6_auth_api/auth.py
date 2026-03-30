import requests
from requests_oauth2 import OAuth2BearerToken
from requests.auth import HTTPDigestAuth, HTTPBasicAuth

user = 'roma1'
passwd = '123'

# Basic auth.
url = f"https://httpbin.org/basic-auth/{user}/{passwd}"
basic = HTTPBasicAuth('roma1', '123')
response = requests.get(url, auth=basic)
print(response.status_code)

# Bearer
url = "https://httpbin.org/bearer"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6InJvbWExIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.PJpvreozcDd4-QjiKIMSmRU4BLFwmVaQCDDjViW-BS4"
headers = { "Authorization": f"Bearer {token}" }
response = requests.get(url, headers=headers)
print(response.status_code)

# Digest-auth
url = f"https://httpbin.org/digest-auth/auth/{user}/{passwd}"
response = requests.get(url, auth=HTTPDigestAuth('roma1', '123')) 
print(response.status_code)

