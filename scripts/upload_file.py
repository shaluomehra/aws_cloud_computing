import boto3

# Initialise S3 client
s3 = boto3.client('s3')

# Define the bucket and file names
bucket_name = 'tech254-shaluo-bucket'
local_file_path = 'local-file.txt'
s3_file_name = 'uploaded-file.txt'

# Upload the file to the bucket
s3.upload_file(local_file_path, bucket_name, s3_file_name)

