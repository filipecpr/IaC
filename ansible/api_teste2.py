import requests

url = "https://api.api-futebol.com.br/v1/campeonatos"

headers = {
    'Authorization': "Bearer test_19114f3348d10612fe244796b45342",


    }

response = requests.request("GET", url, headers=headers)

print(response.text)
