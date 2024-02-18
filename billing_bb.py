import json

import requests
import os
from random import randint
import dotenv

dotenv.load_dotenv()

AUTHENTICATION_URL = "https://oauth.hm.bb.com.br/oauth/token"
BASE_URL = "https://api.hm.bb.com.br/cobrancas/v2"


def get_token(scope_info=True):
    key = os.getenv('KEY')
    id_client = os.getenv('IDCLIENT')
    id_client_secret = os.getenv('IDCLIENTSECRET')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': key,
        'Cache-Control': 'no-cache',
    }
    params = {
        'grant_type': 'client_credentials',
        'client_id': id_client,
        'client_secret': id_client_secret,
        'scope': 'cobrancas.boletos-info' if scope_info == True else 'cobrancas.boletos-requisicao'
    }

    response = requests.post(AUTHENTICATION_URL, params=params, headers=headers)

    if response.status_code != 200:
        return f'Error: {response.content}'

    resultado = response.json()
    return "Bearer " + resultado['access_token']


def get_invoices(situation, agency, account):
    token = get_token()
    application_key = os.getenv('APPLICATION_KEY')

    headers = {
        'Authorization': token,
        'X-Developer-Application-Key': application_key,
        'Accept': 'application/json',
    }

    params = {
        'indicadorSituacao': situation,
        'agenciaBeneficiario': agency,
        'contaBeneficiario': account,
    }

    response = requests.get(BASE_URL + '/boletos', params=params, headers=headers)

    return response.content


if __name__ == '__main__':
    print(get_invoices('A', 452, 123873))
