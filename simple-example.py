import requests

API_BASE = 'https://api.sms-io.ru/sms-api/v1/message/'
API_TOKEN = '_YOUR_TOKEN_HERE_'

headers = {
    'Authorization': 'Token {}'.format(API_TOKEN)
}
message = {
    'external_id': 'client_generated_id',
    'to_number': '+71111111111',
    'text': 'Hello!',
}

response = requests.post(API_BASE, message, headers=headers)
