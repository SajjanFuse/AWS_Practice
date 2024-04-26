import boto3 

local_file = 'linear_model.pkl'
bucket_name = 'sajjan-trainee-filelist'
file_key = 'linear_model.pkl'

s3_client = boto3.client('s3')

try:
    s3_client.upload_file(local_file, bucket_name, file_key)
    print(f'File {local_file} uploaded successfully')

except Exception as e:
    print(e)