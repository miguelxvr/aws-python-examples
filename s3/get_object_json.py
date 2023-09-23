import boto3
import json

# Defina o nome do bucket e o caminho do objeto que você deseja obter
bucket_name = 'nome-do-seu-bucket'
key_name = 'caminho/do/objeto/no/s3.json'

# Crie um cliente s3
s3_client = boto3.client('s3')

try:
    # Obtenha o objeto
    response = s3_client.get_object(Bucket=bucket_name, Key=key_name)
    
    # Leia o conteúdo do objeto
    json_content = response['Body'].read().decode('utf-8')
    
    # Transforme a string JSON em um objeto Python
    data_obj = json.loads(json_content)

    # Agora você pode trabalhar com o objeto `data_obj` como um dicionário Python, lista, etc.
    print(data_obj)
except Exception as e:
    print(f"Erro ao obter o objeto JSON: {e}")
