import boto3
import csv
import os
from botocore.exceptions import ClientError
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def s3_fuction(writer):

	empty_csv_disct = {}

	client = boto3.client('s3', aws_access_key_id="", aws_secret_access_key="")

	s3_response = client.list_buckets()

	for new_var in s3_response['Buckets']:
		
		empty_csv_disct["Bucket_name"] = new_var['Name']
		empty_csv_disct["Created_date"] = new_var['CreationDate']
		writer.writerow(empty_csv_disct)

def send_mail_to_user(file_name):
	SENDER = "nuthalapatashok@gmail.com"
	RECIPIENT = "nuthalapatashok@gmail.com"
	SUBJECT = "RMG auto sending report"
	ATTACHMENT = file_name
	BODY_HTML = """\
	<html>
	<head></head>
	<body>
	<h3>Hi All</h3>
	<p>Please see the attached file for a list of Accesskey those are created 150days ago.</p>
	</body>
	</html>
	"""
	CHARSET = "utf-8"
	client = boto3.client('ses')
	msg = MIMEMultipart('mixed')
	msg['Subject'] = SUBJECT 
	msg['From'] = SENDER 
	msg['To'] = RECIPIENT
	
	msg_body = MIMEMultipart('alternative')
	htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
	msg_body.attach(htmlpart)
	att = MIMEApplication(open(ATTACHMENT, 'rb').read())
	att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
	msg.attach(msg_body)
	msg.attach(att)
	try:
	    response = client.send_raw_email(
	        Source=SENDER,
	        Destinations=[
	            RECIPIENT
	        ],
	        RawMessage={
	            'Data':msg.as_string(),
	        }
	    ) 
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])


def excel_csv_fun():
	fieldnames = ["Bucket_name", "Created_date"]
	file_name = "empty_csv_disct.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		s3_fuction(writer)
	send_mail_to_user(file_name)

def lambda_handler(event, context):
	excel_csv_fun()


