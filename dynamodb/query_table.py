import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Definindo os valores para a chave de partição e chave de classificação
table_name = 'users'
partition_key_value = "joao.silva"
sort_key_value = "Silva"

# Consulta na tabela usando as chaves
try:
    response = dynamodb_client.query(
        TableName=table_name,
        KeyConditionExpression="username = :username_value AND last_name = :last_name_value",
        ExpressionAttributeValues={
            ":username_value": {"S": partition_key_value},
            ":last_name_value": {"S": sort_key_value}
        }
    )

    items = response['Items']
    for item in items:
        print(item)
except Exception as e:
    print(f"Erro ao consultar tabela: {e}")


