import boto3

# Defina nome do bucket e caminho do objeto que você deseja baixar
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/do/objeto/no/s3.txt'
download_path = 'caminho/onde/salvar/no/seu/computador.txt'

# Crie um cliente s3
s3_client = boto3.client('s3')

try:
    # Faça o download do objeto
    s3_client.download_file(bucket_name, key_name, download_path)
    print(f"Download completo: {key_name} para {download_path}.")
except Exception as e:
    print(f"Erro no download: {e}")

