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


def register_invoice(invoice_info):
    token = get_token(scope_info=False)
    application_key = os.getenv('APPLICATION_KEY')

    headers = {
        'Authorization': token,
        'X-Developer-Application-Key': application_key,
        'Accept': 'application/json',
    }

    response = requests.post(BASE_URL + '/boletos', data=json.dumps(invoice_info), headers=headers)
    return response.content


if __name__ == '__main__':
    body_request = {
      "numeroConvenio": 3128557,
      "numeroCarteira": 17,
      "numeroVariacaoCarteira": 35,
      "codigoModalidade": 1,
      "dataEmissao": "15.02.2024",
      "dataVencimento": "31.03.2024",
      "valorOriginal": 123.45,
      "valorAbatimento": 12.34,
      "quantidadeDiasProtesto": 0,
      "quantidadeDiasNegativacao": 0,
      "orgaoNegativador": 10,
      "indicadorAceiteTituloVencido": "S",
      "numeroDiasLimiteRecebimento": 1,
      "codigoAceite": "N",
      "codigoTipoTitulo": 2,
      "descricaoTipoTitulo": "DM",
      "indicadorPermissaoRecebimentoParcial": "S",
      "numeroTituloBeneficiario": "2A584SDGTE8JN2G",
      "numeroTituloCliente": "00031285570689531552",
      "desconto": {
        "tipo": 2,
        "dataExpiracao": "28.02.2024",
        "porcentagem": 5
      },
      "segundoDesconto": {
        "dataExpiracao": "10.03.2024",
        "porcentagem": 4
      },
      "terceiroDesconto": {
        "dataExpiracao": "20.03.2024",
        "porcentagem": 3
      },
      "jurosMora": {
        "tipo": 2,
        "porcentagem": 1.00
      },
      "multa": {
        "tipo": 1,
        "data": "01.04.2024",
        "valor": 10.00
      },
      "pagador": {
        "tipoInscricao": 1,
        "numeroInscricao": 97965940132,
        "nome": "Odorico Paraguassu",
        "endereco": "Avenida Dias Gomes 1970",
        "cep": 77458000,
        "cidade": "Sucupira",
        "bairro": "Centro",
        "uf": "TO",
        "telefone": "63987654321"
      },
      "beneficiarioFinal": {
        "tipoInscricao": 2,
        "numeroInscricao": 74910037000193,
        "nome": "Dirceu Borboleta"
      },
      "indicadorPix": "N"
    }

    print(get_invoices('A', 452, 123873))
    print(register_invoice(body_request))
