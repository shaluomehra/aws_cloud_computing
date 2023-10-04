#  aws s3 rm s3://tech254-shaluo-bucket/uploaded-file.txt

import boto3

# Initialise S3 client
s3 = boto3.client('s3')

# Define the bucket name
bucket_name = 'tech254-shaluo-bucket'

# Delete the bucket (only if it's empty)
s3.delete_bucket(Bucket=bucket_name)


