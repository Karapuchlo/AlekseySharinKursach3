import json, requests
import random

def print_last_five_operations(operations):
    # 5 последних операций
    count = 0
    for operation in operations:
        if operation['state'] == 'EXECUTED':
            date = operation['date'].split('T')[0]
            date = date.split('-')[2] + '.' + date.split('-')[1] + '.' + date.split('-')[0]
            print(date, operation['description'])
            if "from" in operation.keys():
                from_card = operation['from'][:4] + ' ' + operation['from'][4:8] + ' **** ' + operation['from'][-4:]
            to_account = '**' + operation['to'][-4:]
            print(from_card, '->', to_account)
            amount, currency = operation['operationAmount']
            print(amount, currency)

            count += 1

        if count == 5: break

def load_operations(filename):
    f = requests.get(filename)
    data = json.loads(f.text)
    return data


