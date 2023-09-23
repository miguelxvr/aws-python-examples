import boto3

# Inicializa o cliente do S3
s3_client = boto3.client('s3')

# Nome do bucket
bucket_name = 'nome-do-seu-bucket'

try:
    # Deleta o bucket
    s3_client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deletado com sucesso!")

except s3_client.exceptions.NoSuchBucket:
    print(f"Bucket {bucket_name} não existe.")
except s3_client.exceptions.BucketNotEmpty:
    print(f"Bucket {bucket_name} não está vazio. Remova todos os objetos primeiro.")
except Exception as e:
    print(f"Erro ao deletar o bucket: {e}")

