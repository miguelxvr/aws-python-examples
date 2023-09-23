import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Lista de usernames a serem buscados
usernames_to_get = ['joao.silva', 'maria.pereira', 'ana.santos', 'pedro.souza']

# Converta a lista de usernames em uma lista de dicionários de chaves
keys_to_get = [{'username': {'S': username}} for username in usernames_to_get]

response = dynamodb_client.batch_get_item(
    RequestItems={
        table_name: {
            'Keys': keys_to_get
        }
    }
)

items = response['Responses'][table_name]
for item in items:
    print(item)

