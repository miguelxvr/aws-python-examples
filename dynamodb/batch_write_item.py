import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Itens a serem inseridos
items_to_put = [
    {
        'PutRequest': {
            'Item': {
                'username': {'S': 'joao.silva'},
                'last_name': {'S': 'Silva'},
                'age': {'N': '30'}
            }
        }
    },
    {
        'PutRequest': {
            'Item': {
                'username': {'S': 'maria.pereira'},
                'last_name': {'S': 'Pereira'},
                'age': {'N': '28'}
            }
        }
    }
]

response = dynamodb_client.batch_write_item(
    RequestItems={
        table_name: items_to_put
    }
)

# Verifica se houve algum item não processado (em caso de excesso de provisionamento, por exemplo)
unprocessed_items = response['UnprocessedItems']
if unprocessed_items:
    print("Itens não processados:", unprocessed_items)
else:
    print("Todos os itens foram inseridos com sucesso!")
