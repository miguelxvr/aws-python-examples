import boto3

# Crie um cliente S3
s3 = boto3.client('s3')

# Listar os buckets do S3
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(bucket['Name'])
