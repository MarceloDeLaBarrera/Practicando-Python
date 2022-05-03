import requests


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNDgzLCJ1c2VybmFtZSI6Im1hcmNlbG8uZGVsYWJhcnJlcmFAbWFpbC51ZHAuY2wiLCJleHAiOjE2MzU4MjUwMTYsImVtYWlsIjoibWFyY2Vsby5kZWxhYmFycmVyYUBtYWlsLnVkcC5jbCJ9.YaoLhWSB-uaUUX1Y1H0X-XWz72Glv-R3qP7GTfE-g1Q"
url = "http://dogs.magnet.cl/api/v1/breeds/"
headers = {'Authorization': 'JWT {}'.format(token)}
response = requests.get(url, headers=headers)
print(response)
