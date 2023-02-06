import json, requests
import random

def print_last_five_operations(operations):
    # 5 последних операций
    count = 0
    executed_operations = []
    for operation in operations:
        if operation['state'] == 'EXECUTED':
            executed_operations.append(operation)

            executed_operations.sort(key=lambda x: x['date'], reverse=True)

            for i in range(min(5, len(executed_operations))):
                operation = executed_operations[i]

                date = operation['date'].split('T')[0]
                date = date.split('-')[2] + '.' + date.split('-')[1] + '.' + date.split('-')[0]
                description = operation['description']
                if "from" in operation.keys():
                    from_account = mask_account(operation['from'])
                to_account = mask_account(operation['to'])
                amount = operation['operationAmount']['amount']
                currency = operation['operationAmount']['currency']['name']



        count += 1

        if count == 6: break
        print('{} {}'.format(date, description))
        print('{} -> {}'.format(from_account, to_account))
        print(amount, currency)
        print()
def mask_account(number):  # Замаскировать номер счета/карты.
    if len(number) == 16:  # Visa/Mastercard.
        return '{} **** {}'.format(' '.join([number[:4], number[8:12]]), number[-4:])

    elif len(number) == 20:  # Maestro.
        return '{} **** **** {}'.format(' '.join([number[:4], number[8:12]]), number[-4:])

    else:  # Номер счета.
        return '**{}'.format(number[-4:])


def load_operations(filename):
    f = requests.get(filename)
    data = json.loads(f.text)
    return data


