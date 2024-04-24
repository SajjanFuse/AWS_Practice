"""
Listing files in AWS Bucket
"""
import boto3 

s3 = boto3.client('s3')

bucket_name = "sajjan-apprenticetraining-data-demo"

response = s3.list_objects(Bucket=bucket_name)

for file in response['Contents']:
    print(file['Key'])