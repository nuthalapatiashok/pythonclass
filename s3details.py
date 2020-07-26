#List S3 bucket

import boto3
import sys

region = sys.argv[1]
accesskey = sys.argv[2]
secretkey = sys.argv[3]


s3_details = boto3.client('s3',region_name= region,aws_access_key_id= accesskey, aws_secret_access_key= secretkey)

response_s3details = s3_details.list_buckets()
#print (response_s3details['Buckets'])
for each_bucket  in response_s3details['Buckets']:
	print  each_bucket['Name'],each_bucket['CreationDate']
	#print each_bucket['CreationDate']
