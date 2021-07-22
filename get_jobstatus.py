#!/usr/bin/env python
import requests
import json

url = 'http://192.168.99.102:31964/api/v2/'

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

print(users.keys())

### List organizations
response = requests.get(url + "organizations/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

data = response.json()
organizations = {}
for i in range(len(data["results"])):
    organization = data["results"][i]
    organizations[organization["id"]] = organizations

print(organizations.keys())

#### View statistics for job runs for graphing
response = requests.get(url + "dashboard/graphs/jobs/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
if response.status_code != 200:
    #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    print('Status:', response.status_code)
    #exit()

data = response.json()
print(data)
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
    print(data)

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
    print(data)

### List jobs
response = requests.get(url + "jobs/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    #exit()

data = response.json()
print(data)
jobs = {}
for i in range(len(data["results"])):
    job = data["results"][i]
    jobs[job["id"]] = job

print(jobs.keys())

### List activity streams for a job
for i in jobs.keys():
    params = {
        "id": i
    }

    print('jobID:', i, ' name of this job:', jobs[i]["name"], '\n')
    response = requests.get(url + "jobs/" + str(i) + "/activity_stream/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(data)

### List job events for a job
for i in jobs.keys():
    params = {
        "id": i
    }

    print('jobID:', i, ' name of this job:', jobs[i]["name"], '\n')
    response = requests.get(url + "jobs/" + str(i) + "/job_events/", auth=('sj-swe', 'sj-swe'), headers=headers, verify=False)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
        #exit()

    data = response.json()
    print(data)















