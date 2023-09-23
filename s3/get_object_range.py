import boto3

# Defina o nome do bucket e o caminho do objeto que você deseja obter
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/do/objeto/no/s3'

# Inicializa o cliente s3
s3_client = boto3.client('s3')

# Defina o intervalo de bytes que você deseja obter.
# Por exemplo, para obter os bytes de 0 a 99 (os primeiros 100 bytes):
byte_range = 'bytes=0-99'

try:
    # Faça uma solicitação GET com o cabeçalho Range
    response = s3_client.get_object(Bucket=bucket_name, Key=key_name, Range=byte_range)

    # Leia a parte do objeto
    part_data = response['Body'].read().decode('utf-8')
    print(part_data)
except Exception as e:
    print(f"Erro ao obter a parte do objeto: {e}")

