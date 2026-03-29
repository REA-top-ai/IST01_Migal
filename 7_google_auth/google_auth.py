import requests
from requests_oauth2 import OAuth2BearerToken
from requests.auth import HTTPDigestAuth, HTTPBasicAuth

token = '4/0Aci98E_QcpIiE_UjtOVME1VexbPYBCOKZ7Es5HCbs3VYs1qxPJpOgGHxODMKH1f_CgV04g'
url = "https://google.com/"
token = OAuth2BearerToken(f'Bearer {token}')
response = requests.get(url, auth=token)
print(response)
