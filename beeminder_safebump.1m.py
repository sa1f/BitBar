#!/usr/bin/python

import os
import requests
import json

info = {};

configPath = "/Users/saif/Dropbox/Apps/BitBar/config/"

if not os.path.isfile(configPath + 'beeminder_info.json'):
    print "Sign into beeminder and visit: https://www.beeminder.com/api/v1/auth_token.json"
    info['username'] = raw_input("Enter your username: ")
    info['auth_token'] = raw_input("Enter your auth_token code: ")
    info['goal_name'] = raw_input("Enter your goal name: ")
    with open('beeminder_info.json', 'w') as outfile:
        json.dump(info, outfile)

with open(configPath + 'beeminder_info.json', 'r') as infile:
    info = json.load(infile)

params = {'auth_token': info['auth_token']}
baseUrl = baseUrl = "https://www.beeminder.com/api/v1/" + "users/" + info['username']
r = requests.get(baseUrl + "/goals/" + info['goal_name'] + ".json", params=params)

print r.json()['lanewidth'] - r.json()['delta']