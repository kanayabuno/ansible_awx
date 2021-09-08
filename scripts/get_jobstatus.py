#!/usr/bin/env python
import requests
import json

url = 'http://192.168.99.102:31964/api/v2/'
user = 'sj-swe'
password = 'sj-swe'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

### list users
response = requests.get(url + "users/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

data = response.json()
users = {}
for i in range(len(data["results"])):
    user = data["results"][i]
    users[user["id"]] = user

#print(users.keys())

### List organizations
response = requests.get(url + "organizations/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

print(response.request.url)
print(response.request.body)
print(response.request.headers)
data = response.json()
organizations = {}
for i in range(len(data["results"])):
    organization = data["results"][i]
    organizations[organization["id"]] = organizations

#print(organizations.keys())

### List inventories
response = requests.get(url + "inventories/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

data = response.json()
inventories = {}
for i in range(len(data["results"])):
    inventory = data["results"][i]
    inventories[inventory["id"]] = inventory

#print(inventories.keys())


#### View statistics for job runs for graphing
response = requests.get(url + "dashboard/graphs/jobs/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

data = response.json()
print(json.dumps(data))
print()

# List activity streams for an organization
for i in organizations.keys():
    params = {
        "id": i
    }

    response = requests.get(url + "organizations/" + str(i) + "/activity_stream/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(json.dumps(data, indent=1))

print()

# List activity streams for an User
for i in users.keys():
    params = {
        "id": i
    }

    print('UserID:', i, ' Username:', users[i]["username"], '\n')
    response = requests.get(url + "users/" + str(i) + "/activity_stream/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(json.dumps(data, indent=1))

### List jobs
response = requests.get(url + "jobs/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

data = response.json()
print(json.dumps(data, indent=1))

jobs = {}
for i in range(len(data["results"])):
    job = data["results"][i]
    jobs[job["id"]] = job

#print(jobs.keys())

### Get job status
for i in jobs.keys():
    params = {
        "id": i
    }

    print('jobID:', i, ' name of this job:', jobs[i]["name"], '\n')

    ### List activity streams for a job
    response = requests.get(url + "jobs/" + str(i) + "/activity_stream/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(json.dumps(data, indent=1), '\n')

    ### List job events for a job
    response = requests.get(url + "jobs/" + str(i) + "/job_events/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(json.dumps(data, indent=1), '\n')

    ### List job host summaries for a job
    response = requests.get(url + "jobs/" + str(i) + "/job_host_summaries/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(json.dumps(data, indent=1), '\n')

    ### List Labels for a job
    response = requests.get(url + "jobs/" + str(i) + "/labels/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(json.dumps(data, indent=1), '\n')

### List activity streams for an inventory
for i in inventories.keys():
    params = {
        "id": i
    }

    print('inventoryID:', i, ' Name:', inventories[i]["name"], '\n')
    response = requests.get(url + "inventories/" + str(i) + "/activity_stream/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(json.dumps(data, indent=1))
