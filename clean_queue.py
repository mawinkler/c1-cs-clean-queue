import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import json
from os import getenv

username = getenv('USERNAME')
password = getenv('PASSWORD')
url = getenv('URL')

large_number = 1000

payload = {
    "user": {
        "userID": username,
        "password": password
    }
}
post_header = {
    "Content-type": "application/json",
    "x-argus-api-version": "2017-10-16",
}

session = requests.post(f"https://{url}/api/sessions", data=json.dumps(payload), headers=post_header, verify=False)
token =  json.loads(session.text)["token"]

post_header = {
    "Content-type": "application/json",
    "authorization": "Bearer " + token
}

counter = 0

while (True):
    scans_body = requests.get(f"https://{url}/api/scans?status=pending&limit={large_number}", headers=post_header, verify=False)
    scans = json.loads(scans_body.text)['scans']

    if (len(scans) == 0):
        break

    for scan in scans:
        current_scan = scan['href']
        print(f"deleting scan {current_scan}")
        requests.delete(f"https://{url}{current_scan}", headers=post_header, verify=False)
        counter += 1
    
    print(f"paging")

print(f"cleaned {counter} scans")
