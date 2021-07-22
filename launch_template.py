#!/usr/bin/env python
import requests
import json

url = 'http://192.168.99.100:31964/api/v2/'
user = 'kana'
pwd = 'kana'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}
# Do the HTTP request
response = requests.get(url + "inventories/", auth=(user, pwd), headers=headers, verify=False)
# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    exit()
# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data["results"][0]["name"])

#data = {
#  "email": "a@a.com",
#  "first_name": "a",
#  "is_superuser": True,
#  "last_name": "a",
#  "password": "temple123",
#  "username": "allied"
#}
#
## create a new user
#response = requests.post(url + "users/", auth=(user, pwd), headers=headers, json=data, verify=False)
#if response.status_code != 200:
#    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
#    exit()

data = {
    "name": "second project",
    "scm_types": "git",
    "scm_url": "https://github.com/kanayabuno/ansible_awx",
    "organization": "2",
    "timeout": 10
}

# Create a new project
#response = requests.post(url + "projects/", auth=(user, pwd), headers=headers, json=data, verify=False)
#if response.status_code != 200:
#    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
#    exit()

#project_id = response.id

## Update an existing project
#response = requests.post(url + "projects/17", auth=(user, pwd), headers=headers, json=data, verify=False)
#print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)

## Get a list of templates
#response = requests.get(url + "job_templates/", auth=(user, pwd), headers=headers, verify=False)
## Check for HTTP codes other than 200
#if response.status_code != 200:
#    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
#    exit()
## Decode the JSON response into a dictionary and use the data
#data = response.json()
#print(data)




