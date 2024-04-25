import boto3 

local_file = 'tensorflow_model.pkl'
bucket_name = 'sajjan-trainee-filelist'
file_key = 'tensorflow_model.pkl'

s3_client = boto3.client('s3')

try:
    s3_client.upload_file(local_file, bucket_name, file_key)
    print(f'File {local_file} uploaded successfully')

except Exception as e:
    print(e)