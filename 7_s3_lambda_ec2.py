import json 
import boto3 

def lambda_handler(event, context):
    """Processes S3 PutObject events and starts an EC2 instance."""
    # Extract bucket and file information from the event
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']

        # Configure EC2 launch parameters (replace with your details)
        image_id = "ami-0123456789abcdef0"  # Replace with your AMI ID
        instance_type = "t2.micro"  # Replace with your desired instance type
        security_group_id = "sg-12345678"  # Replace with your security group ID
        key_name = "your-key-pair-name"  # Replace with your key pair name

        # Create EC2 client and launch an instance
        ec2_client = boto3.client('ec2')

        try:
            response = ec2_client.run_instances(
                ImageId=image_id,
                MinCount=1,
                MaxCount=1,
                InstanceType=instance_type,
                KeyName=key_name,
                SecurityGroupIds=[security_group_id]
            )
        except Exception as e:
            pass
    return {
      'statusCode': 200,
      'body': f'File upload processed. EC2 instance launch initiated.'
    }
    