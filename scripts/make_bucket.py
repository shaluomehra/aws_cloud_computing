import boto3

s3 = boto3.resource('s3')

s3.create_bucket(Bucket='tech254-shaluo-bucket', CreateBucketConfiguration={'LocationConstraint':'eu-west-1'})
