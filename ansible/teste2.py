import requests

url = "https://api-football-v1.p.rapidapi.com/v2/leagues"

headers = {
    'x-rapidapi-key': "a0e299c1ffmsh226ceb2efe43236p19841ejsna1861fcae011",
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
