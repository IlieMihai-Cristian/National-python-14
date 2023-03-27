# import requests
#
# url = "https://v6.exchangerate-api.com/v6/4c7c987629a9daf434ac285c/latest/EUR"
#
# payload = ""
# headers = {
#   'Authorization': 'Token 4c7c98762a9daf434ac25c'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

import requests

url = "https://findwork.dev/api/jobs/"

payload = {
  "location": "Bucharest"
}
headers = {
  'Authorization': 'Token f7910b6b4fee8499d512a0b0a5b750d6b6b3e1c8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())