"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Compute Engine API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/compute
2. This sample uses Application Default Credentials for authentication.
   If not already done, install the gcloud CLI from
   https://cloud.google.com/sdk and run
   `gcloud beta auth application-default login`.
   For more information, see
   https://developers.google.com/identity/protocols/application-default-credentials
3. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint
from google.oauth2 import service_account
from googleapiclient import discovery
#from oauth2client.client import GoogleCredentials

#credentials = GoogleCredentials.get_application_default()
credentials = service_account.Credentials.from_service_account_file(filename="gcp.json", scopes=['https://www.googleapis.com/auth/cloud-platform'])
service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'bubbyproject-344809'  # TODO: Update placeholder value.

network_body = {
        "name": 'py-vnet',
        "network": '10.0.0.0/16',
        "region": 'europe-west1'
}

request = service.networks().list(project=project)
response = request.execute()

# TODO: Change code below to process the `response` dict:
#pprint("response", response)
for network in response['items']:
        # TODO: Change code below to process each `network` resource:
        print(network)










'''
https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert
'''
from pprint import pprint
from google.oauth2 import service_account
from googleapiclient import discovery

#credentials = service_account.Credentials.from_service_account_file(filename=r"C:\Users\jyoth\OneDrive\Desktop\CSP/gcp/gcp.json", scopes=['https://www.googleapis.com/auth/cloud-platform'])
credentials = service_account.Credentials.from_service_account_file(filename=r"./gcp.json", scopes=['https://www.googleapis.com/auth/cloud-platform'])
project = 'josephproject' # Project ID for this request
vpc_service = discovery.build('compute', 'v1', credentials=credentials)
network_body = {
        "name": 'py-vnet',
        "network": '10.0.0.0/16',
        "region": 'us-east1',
        "autoCreateSubnetworks": True,
}
request = vpc_service.networks().insert(project=project, body=network_body)
response = request.execute()
pprint(response)
