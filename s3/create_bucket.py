import boto3

# Cria um cliente S3
s3 = boto3.client('s3')

# Defina o nome do bucket
bucket_name = "meu-novo-bucket-unico"

try:
    # Cria um bucket
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar bucket: {e}")

