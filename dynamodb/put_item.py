import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Define o item a ser inserido
item = {
    'username': {'S': 'joao.silva'},
    'first_name': {'S': 'João'},
    'last_name': {'S': 'Silva'},
    'age': {'N': '25'},
    'account_type': {'S': 'standard_user'}
}

try:
    # Insere o item na tabela
    response = dynamodb_client.put_item(TableName=table_name, Item=item)
    print(f"Item inserido com sucesso na tabela {table_name}!")
except dynamodb_client.exceptions.ResourceNotFoundException:
    print(f"A tabela {table_name} não foi encontrada.")
except Exception as e:
    print(f"Erro ao inserir item: {e}")

