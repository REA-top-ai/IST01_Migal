import requests
from requests_oauth2 import OAuth2BearerToken
from requests.auth import HTTPDigestAuth, HTTPBasicAuth

# Basic auth.
url = "https://httpbin.org/basic-auth/roma1/123"
basic = HTTPBasicAuth('roma1', '123')
response = requests.get(url, auth=basic)
print(response)

# Bearer
url = "https://httpbin.org/bearer"
token = OAuth2BearerToken('Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6InJvbWExIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.PJpvreozcDd4-QjiKIMSmRU4BLFwmVaQCDDjViW-BS4')
response = requests.get(url, auth=token)
print(response)

# Digest-auth
url = "https://httpbin.org/digest-auth/auth/roma1/123"
basic = HTTPDigestAuth('roma1', '123')
response = requests.get(url, auth=basic) 
print(response)

