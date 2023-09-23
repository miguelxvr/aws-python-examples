import boto3

# Defina o nome do bucket e o caminho do objeto que deseja enviar
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/onde/quer/salvar/no/s3.zip'
file_path = 'caminho_do_seu_arquivo.zip'

# Crie um cliente s3
s3_client = boto3.client('s3')

try:
    # Faça o upload do arquivo
    s3_client.upload_file(file_path, bucket_name, key_name)
    print(f"Upload completo: {key_name} para {bucket_name}.")
except Exception as e:
    print(f"Erro no upload: {e}")

