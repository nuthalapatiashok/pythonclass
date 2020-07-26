import boto3

iam_allcomands = boto3.client('iam', aws_access_key_id= "AKIAVCPCFOO6OGSH7WSU", aws_secret_access_key= "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")


list_users_response  = iam_allcomands.list_users()
#print (list_users_response['Users'])

for new_var in list_users_response['Users']:
  print (new_var['UserName'],new_var['CreateDate'])
    