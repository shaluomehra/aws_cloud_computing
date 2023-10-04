import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define the bucket and file names
bucket_name = 'tech254-shaluo-bucket'
s3_file_name = 'uploaded-file.txt'
local_file_path = 'downloaded-file.txt'

# Download the file from the bucket
s3.download_file(bucket_name, s3_file_name, local_file_path)
