
#List VPC
import boto3
ec2 = boto3.resource('ec2',region_name="us-west-1",aws_access_key_id= "AKIAVCPCFOO6I6LOEE2I", aws_secret_access_key= "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")
vpc_client = boto3.client('ec2',region_name="us-west-1",aws_access_key_id= "AKIAVCPCFOO6I6LOEE2I", aws_secret_access_key= "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")
response_vpc = vpc_client.describe_vpcs()
#print response_vpc['Vpcs']
for each_vpc in response_vpc['Vpcs']:
 	print ("Vpc id  ==> {0}".format (each_vpc['VpcId']))
