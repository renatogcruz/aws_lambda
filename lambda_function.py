import json
# Assumindo que você tenha um arquivo chamado "log.py" no mesmo diretório
from log import log


def lambda_handler(event, context):
    # TODO implement

    print(f'Log primeira funcao: {event}')

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


print(lambda_handler('evento de ativação', None))
