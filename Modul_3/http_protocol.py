# import http.client
# conn = http.client.HTTPConnection("www.example.com")
# conn.request("GET", "/")
#
# response = conn.getresponse()
# print(response.status, response.reason)
# print(response.read().decode("utf-8"))
# conn.close()
#
# print("_____________________________")
#
# import requests
#
# response = requests.get("https://www.example.com")
# print(response.status_code)
# print(response.text)

import requests

data = {"key": "value"}

response = requests.post("https://www.example.com/post", data=data)

print(response.status_code)
print(response.text)