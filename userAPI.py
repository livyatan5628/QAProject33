import requests
import json
import tests_deposit250
url = "https://reqres.in/api/users/22"
response =requests.get(url)
user22 = response.json()
print(user22)
def checkStatusCode(url):
    response = requests.get(url)
    return 400 > response.status_code >= 200

