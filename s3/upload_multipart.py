import boto3
from boto3.s3.transfer import TransferConfig, S3Transfer

# Configurações para o upload
local_file_path = 'caminho_do_seu_arquivo_grande.zip'
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/onde/quer/salvar/no/s3.zip'
threshold_size = 8 * 1024 * 1024  # Utilizar partes de 8MB

# Cria um cliente S3
client = boto3.client('s3')

# Configuração para upload multi-part
config = TransferConfig(multipart_threshold=threshold_size)

# Inicializa o transferência
transfer = S3Transfer(client, config)

# Realiza o upload
try:
    transfer.upload_file(local_file_path, bucket_name, key_name)
    print(f"Upload completo: {key_name} para {bucket_name}.")
except Exception as e:
    print(f"Erro no upload: {e}")

