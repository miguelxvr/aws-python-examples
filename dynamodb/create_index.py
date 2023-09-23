import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

try:
    # Cria o GSI na tabela existente
    response = dynamodb_client.update_table(
        TableName=table_name,
        AttributeDefinitions=[
            {
                'AttributeName': 'email',
                'AttributeType': 'S'  # Tipo de atributo: String
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'  # Tipo de atributo: String
            }
        ],
        GlobalSecondaryIndexUpdates=[
            {
                'Create': {
                    'IndexName': 'email-index',
                    'KeySchema': [
                        {
                            'AttributeName': 'email',
                            'KeyType': 'HASH'  # Chave de partição
                        },
                        {
                            'AttributeName': 'last_name',
                            'KeyType': 'RANGE'  # Chave de classificação
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 5,
                        'WriteCapacityUnits': 5
                    }
                }
            }
        ]
    )

    print(f"GSI 'email-index' criado com sucesso para a tabela {table_name}!")
except dynamodb_client.exceptions.ResourceNotFoundException:
    print(f"A tabela {table_name} não foi encontrada.")
except Exception as e:
    print(f"Erro ao criar o índice: {e}")
