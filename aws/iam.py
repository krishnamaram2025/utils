import boto3
import os
import sys
from datetime import date

# accesskey = str(sys.argv[1])
# secretkey = str(sys.argv[2])
username = 'admin'

iam_client = boto3.client('iam', region_name = 'us-east-1', aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'])
keys = iam_client.list_access_keys(UserName=username)
print("keys", keys)
for key in keys['AccessKeyMetadata']:
  if key['AccessKeyId'] == os.environ['AWS_ACCESS_KEY_ID']:
    print("key", key)
    accesskeybirthdate = key['CreateDate'].date()
    todaydate = date.today()
    age = todaydate - accesskeybirthdate
    print("age", age.days)
