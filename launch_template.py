import requests

#url = 'http://192.168.49.2:32281/api/v2/me'

url = 'http://192.168.49.2:32281/api/v2/job_templates/12/launch/'
# Eg. User name="admin", Password="admin" for this code sample.
user = 'kana'
pwd = 'kana'
# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}
# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, verify=False)
# Check for HTTP codes other than 200
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response)
    exit()
# Decode the JSON response into a dictionary and use the data
data = response.json()
