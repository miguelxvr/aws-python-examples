import boto3

# Defina o nome do bucket e o caminho do objeto que você deseja excluir
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/do/objeto/no/s3'

# Inicializa o cliente s3
s3_client = boto3.client('s3')

try:
    # Remove o objeto
    s3_client.delete_object(Bucket=bucket_name, Key=key_name)
    print(f"Objeto '{key_name}' removido com sucesso do bucket '{bucket_name}'.")
except Exception as e:
    print(f"Erro ao remover o objeto: {e}")
