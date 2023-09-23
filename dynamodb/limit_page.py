import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Definições da paginação
limit_per_page = 10

# Inicia o LastEvaluatedKey como None para a primeira página
last_evaluated_key = None

while True:
    if last_evaluated_key:
        response = dynamodb_client.scan(
            TableName=table_name,
            Limit=limit_per_page,
            ExclusiveStartKey=last_evaluated_key  # Chave de continuação da página anterior
        )
    else:
        response = dynamodb_client.scan(
            TableName=table_name,
            Limit=limit_per_page
        )

    # Processa os itens retornados
    items = response['Items']
    for item in items:
        print(item)

    # Verifica se há mais páginas a serem lidas
    if 'LastEvaluatedKey' in response:
        last_evaluated_key = response['LastEvaluatedKey']
    else:
        break
