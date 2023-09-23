import boto3

# Defina nome do bucket e caminho do objeto que deseja enviar
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/onde/quer/salvar/no/s3.zip'
file_path = 'caminho_do_seu_arquivo.zip'

# Inicializa o cliente S3
s3_client = boto3.client('s3')

# Define metadados personalizados e faz o upload de um arquivo
s3_client.upload_file(file_path, bucket_name, key_name,
                      ExtraArgs={'Metadata': {'autor': 'João Silva'}})

# Recupera metadados do objeto
response = s3_client.head_object(Bucket=bucket_name, Key=key_name)
metadata = response.get('Metadata', {})
print(metadata)  # Saída: {'autor': 'João Silva'}

