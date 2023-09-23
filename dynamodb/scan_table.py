import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

try:
    # Realiza a varredura na tabela com o filtro aplicado
    response = dynamodb_client.scan(
        TableName=table_name,
        FilterExpression="age > :age_value",
        ExpressionAttributeValues={
            ":age_value": {"N": "25"}
        }
    )
    
    items = response['Items']
    for item in items:
        print(item)
except Exception as e:
    print(f"Erro ao varrer itens: {e}")

