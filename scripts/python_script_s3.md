# Python Scripts using Boto3

## Create a bucket 

To set the s3 interface you will be using `boto3.resource`
```
import boto3

s3 = boto3.resource('s3')

s3.create_bucket(Bucket='tech254-shaluo-bucket', CreateBucketConfiguration={'LocationConstraint':'eu-west-1'})
```
`Bucket='tech254-shaluo-bucket'`: <br> Specifies the name of the bucket to be created, bucket names must be unique across all of AWS <br>

`CreateBucketConfiguration={'LocationConstraint':'eu-west-1'}`: <br> Specifies the region where the bucket should be created. In this case, the region is `'eu-west-1'`.

## Upload a file to bucket
```
import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-shaluo-bucket'
local_file = 'hello.txt'
s3_file_name = 'hello1.txt'

s3.upload_file(local_file, bucket_name, s3_file_name)
```
`bucket_name` is the name of the bucket we want to use <br>
`local_file` is the name of the local file you want to push to the s3 bucket <br>
`s3_file_name` is the name given to the local file once its uploaded onto your bucket <br>

## Download a file to yor instance
```
import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-shaluo-bucket'
s3_file_name = 'uploaded-file.txt'
local_file = 'downloaded-file.txt'

s3.download_file(bucket_name, s3_file_name, local_file)
```

(Opposite of uploading)

## Delete a Bucket

```
import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-shaluo-bucket'

s3.delete_bucket(Bucket=bucket_name)
```

To delete a bucket you need to make sure it's empty first

Use: `aws s3 rm s3://tech254-shaluo-bucket/<uploaded-file.txt>`
to delete files and then delete the bucket once its empty








