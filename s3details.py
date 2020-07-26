#List S3 bucket

import boto3

s3_details = boto3.client('s3',region_name="us-west-1",aws_access_key_id= "AKIAVCPCFOO6I6LOEE2I", aws_secret_access_key= "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")

response_s3details = s3_details.list_buckets()
#print (response_s3details['Buckets'])
for each_bucket  in response_s3details['Buckets']:
	print  each_bucket['Name'],each_bucket['CreationDate']
	#print each_bucket['CreationDate']
