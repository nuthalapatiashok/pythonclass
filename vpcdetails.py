
#List VPC
import boto3
import sys

region = sys.argv[1]
accesskey = sys.argv[2]
secretkey = sys.argv[3]

ec2 = boto3.resource('ec2',region_name= region,aws_access_key_id= accesskey, aws_secret_access_key= secretkey)
vpc_client = boto3.client('ec2',region_name= region,aws_access_key_id= accesskey , aws_secret_access_key= secretkey )
response_vpc = vpc_client.describe_vpcs()
#print response_vpc['Vpcs']
for each_vpc in response_vpc['Vpcs']:
 	print ("Vpc id  ==> {0}".format (each_vpc['VpcId']))
