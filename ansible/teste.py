#!/usr/bin/python3

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "a0e299c1ffmsh226ceb2efe43236p19841ejsna1861fcae011"
    }

conn.request("GET", "/leagues/seasons", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
