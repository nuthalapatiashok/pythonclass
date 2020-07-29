
'''
import boto3

ec2_details = boto3.client('ec2',region_name="us-west-1",aws_access_key_id= "", aws_secret_access_key= "")

instance_response = ec2_details.describe_instances()
#print (instance_response['Reservations'])

for var_value in instance_response['Reservations']:

	for new_var2 in var_value['Instances']:
		print (new_var2['ImageId'],new_var2['PrivateDnsName'],new_var2['InstanceId'])



# This script will create a Ec2 Instance
import boto3

ec2_creation = boto3.client('ec2',region_name="us-west-1",aws_access_key_id= "", aws_secret_access_key= "")

# When we invoke client we always got response back
response = ec2_creation.run_instances(
    ImageId='ami-',
    InstanceType='t2.micro',

    MinCount=1,
    MaxCount=1
)
print(response)

'''


