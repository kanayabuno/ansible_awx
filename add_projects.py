#!/usr/bin/env python
import requests
import json

url = 'http://192.168.99.102:31964/api/v2/'
user = 'kana'
pwd = 'kana'

### Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}


### Create a new project ****even if I select scm type "git", it creates a project with scm type manual****
#response = requests.post(url + "projects/", auth=(user, pwd), headers=headers, json=data, verify=False)
#if response.status_code != 200:
#    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
#    exit()
#
#project_id = response.id


### Get a list of projects
response = requests.get(url + "projects/", auth=(user, pwd), headers=headers, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

project_name = "kana github project"
project_id = 0
data = response.json()

for i in range(len(data["results"])):
    if data["results"][i]["name"] == project_name:
        project_id = data["results"][i]["id"]

print(project_id)
print()

### Add a new inventory
data = {
    "name": "first inventory",
    "organization": "1",
}

response = requests.post(url + "inventories/", auth=(user, pwd), headers=headers, json=data, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

data = response.json()
inventory_id = data["id"]
print(inventory_id)

## Create a new inventory source
data = {
    "name": "kana github source",
    "source": "scm",
    "source_project": project_id,
    "source_path": "hosts",
    "organization": "1",
}

response = requests.post(url + "inventories/" + str(inventory_id) + "/inventory_sources/", auth=(user, pwd), headers=headers, json=data, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()
