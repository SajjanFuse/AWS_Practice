import boto3

BUCKET_NAME = "sajjan-trainee-filelist"
S3_FILE_KEY = "demo_file.py"
LOCAL_FILE_PATH="demo_file.py"


def download_file_from_s3():
    """Downloads a file from S3 to the EC2 instance."""
    try:
        # Use IAM role credentials if available, otherwise use provided credentials
        session = boto3.Session() if 'AWS_ACCESS_KEY_ID' not in locals() else boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        s3_client = session.client('s3')
        s3_client.download_file(BUCKET_NAME, S3_FILE_KEY, LOCAL_FILE_PATH)
        print(f"File downloaded successfully: {LOCAL_FILE_PATH}")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    download_file_from_s3()