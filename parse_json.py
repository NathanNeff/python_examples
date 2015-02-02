#!/bin/env python
import json
data = [ ]
json_data = open('lichess.json')
data = json.load(json_data)
print json.dumps(data, indent=4)

for game in data["list"]:
    print game["id"]

    white = game["players"]["white"]
    black = game["players"]["black"]

    if white:
        print white["userId"]
    if black:
        print black["userId"]

    print "----------------------------------------------------------------------"


