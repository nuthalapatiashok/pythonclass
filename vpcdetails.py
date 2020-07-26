
#List VPC
import boto3
import sys


accesskey = sys.argv[1]
secretkey = sys.argv[2]

ec2 = boto3.resource('ec2',aws_access_key_id= accesskey, aws_secret_access_key= secretkey)
vpc_client = boto3.client('ec2',aws_access_key_id= accesskey , aws_secret_access_key= secretkey )
response_vpc = vpc_client.describe_vpcs()
#print response_vpc['Vpcs']
for each_vpc in response_vpc['Vpcs']:
 	print ("Vpc id  ==> {0}".format (each_vpc['VpcId']))
