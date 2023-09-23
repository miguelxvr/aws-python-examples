import boto3

# Defina o nome do bucket e o caminho do objeto que você deseja obter os metadados
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/do/objeto/no/s3.json'

# Crie um cliente s3
s3_client = boto3.client('s3')

try:
    # Obtenha os metadados do objeto
    response = s3_client.head_object(Bucket=bucket_name, Key=key_name)
    
    # Os metadados personalizados são armazenados sob a chave 'Metadata'
    metadata = response.get('Metadata', {})
    print(metadata)

    # Demais metadados estão disponíveis na resposta. Por exemplo:
    print(f"Size: {response['ContentLength']} bytes")
    print(f"Content Type: {response['ContentType']}")

except Exception as e:
    print(f"Erro ao obter os metadados do objeto: {e}")

