import boto3

# Define nome do bucket e caminho do objeto que deseja enviar
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/onde/quer/salvar/no/s3.txt'
data = "Este é o conteúdo que será enviado para o S3."

# Crie um cliente s3
s3_client = boto3.client('s3')

try:
    # Faça o upload da string diretamente
    s3_client.put_object(Bucket=bucket_name, Key=key_name, Body=data)
    print(f"Upload completo: {key_name} para {bucket_name}.")
except Exception as e:
    print(f"Erro no upload: {e}")
