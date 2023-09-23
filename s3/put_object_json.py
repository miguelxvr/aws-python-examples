import boto3
import json

# Defina o nome do bucket e o caminho do objeto que deseja criar
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/onde/quer/salvar/no/s3.json'
data_obj = {
    "nome": "João",
    "cidade": "São Paulo"
}

# Crie um cliente s3
s3_client = boto3.client('s3')

try:
    # Faça o upload da string JSON diretamente
    s3_client.put_object(Bucket=bucket_name, Key=key_name,
                         Body=json.dumps(data_obj), ContentType='application/json')
    print(f"Upload completo: {key_name} para {bucket_name}.")
except Exception as e:
    print(f"Erro no upload: {e}")

