import json
import requests
import os
import dotenv

dotenv.load_dotenv()


class BBChargingAPI:
    authentication_url = None
    base_url = None

    def __init__(self, test_environment=False):
        if test_environment:
            self.authentication_url = "https://oauth.hm.bb.com.br/oauth/token"
            self.base_url = "https://api.hm.bb.com.br/cobrancas/v2"
        else:
            self.authentication_url = "https://oauth.bb.com.br/oauth/token"
            self.base_url = "https://api.bb.com.br/cobrancas/v2"

    def _get_token(self, scope_info=True):
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
            'scope': 'cobrancas.boletos-info' if scope_info else 'cobrancas.boletos-requisicao'
        }

        response = requests.post(self.authentication_url, params=params, headers=headers)

        if response.status_code != 200:
            return f'Error: {response.content}'

        result = response.json()
        return "Bearer " + result['access_token']

    def get_invoices(self, situation, agency, account):
        token = self._get_token()
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

        response = requests.get(self.base_url + '/boletos', params=params, headers=headers)

        return response.content

    def register_invoice(self, invoice_info):
        token = self._get_token(scope_info=False)
        application_key = os.getenv('APPLICATION_KEY')

        headers = {
            'Authorization': token,
            'X-Developer-Application-Key': application_key,
            'Accept': 'application/json',
        }

        response = requests.post(self.base_url + '/boletos', data=json.dumps(invoice_info), headers=headers)
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
            "numeroInscricao": 74910037000194,
            "nome": "Dirceu Borboleta"
        },
        "indicadorPix": "N"
    }

    bb_charging_api = BBChargingAPI(test_environment=True)
    print(bb_charging_api.get_invoices('A', 452, 123873))
    # print(bb_charging_api.register_invoice(body_request))
