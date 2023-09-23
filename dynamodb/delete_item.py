import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Define a chave primária do item a ser excluído
key = {
    'username': {'S': 'joao.silva'}
}

try:
    # Exclui o item na tabela
    response = dynamodb_client.delete_item(
        TableName=table_name,
        Key=key
    )
    print(f"Item excluído com sucesso da tabela {table_name}!")
except dynamodb_client.exceptions.ResourceNotFoundException:
    print(f"A tabela {table_name} não foi encontrada.")
except Exception as e:
    print(f"Erro ao excluir item: {e}")

