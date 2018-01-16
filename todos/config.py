import os

aws = {
    'region': os.environ['REGION'],
    'dynamodb_host': 'https://dynamodb.' + os.environ['REGION'] + '.amazonaws.com',
    'allow-origin': '*',
}
