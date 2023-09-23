import boto3

# Defina nome do bucket e caminho do objeto que você deseja obter
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/do/objeto/no/s3.txt'

# Crie um cliente s3
s3_client = boto3.client('s3')

try:
    # Obtenha o objeto
    response = s3_client.get_object(Bucket=bucket_name, Key=key_name)
    
    # Leia o conteúdo do objeto
    content = response['Body'].read().decode('utf-8')

    # Print ou processe o conteúdo conforme necessário
    print(content)
except Exception as e:
    print(f"Erro ao obter o objeto: {e}")
