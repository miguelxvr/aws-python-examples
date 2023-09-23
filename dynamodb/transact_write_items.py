import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Lista de operações a serem realizadas como uma transação
transact_items = [
    {
        'Put': {
            'TableName': table_name,
            'Item': {
                'username': {'S': 'joao.silva'},
                'last_name': {'S': 'Silva'},
                'age': {'N': '30'}
            }
        }
    },
    {
        'Update': {
            'TableName': table_name,
            'Key': {
                'username': {'S': 'maria.pereira'},
                'last_name': {'S': 'Pereira'}
            },
            'UpdateExpression': 'SET age = :new_age',
            'ExpressionAttributeValues': {
                ':new_age': {'N': '29'}
            }
        }
    },
    {
        'Delete': {
            'TableName': table_name,
            'Key': {
                'username': {'S': 'ana.santos'},
                'last_name': {'S': 'Santos'}
            }
        }
    }
]

try:
    response = dynamodb_client.transact_write_items(TransactItems=transact_items)
    print("Transação realizada com sucesso!")
except dynamodb_client.exceptions.TransactionCanceledException as e:
    print("Transação foi cancelada:", e)
except Exception as e:
    print(f"Erro ao executar transação: {e}")
