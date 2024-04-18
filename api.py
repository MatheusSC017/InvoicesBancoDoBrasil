import json
import requests
import os
import dotenv
from datetime import timedelta, date
from utils import singleton

dotenv.load_dotenv()


@singleton
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

    def get_invoice(self, agreement, billing_title_number):
        token = self._get_token()
        application_key = os.getenv('APPLICATION_KEY')

        headers = {
            'Authorization': token,
            'X-Developer-Application-Key': application_key,
            'Accept': 'application/json',
        }

        params = {
            'numeroConvenio': agreement,
        }

        response = requests.get(f'{self.base_url}/boletos/{billing_title_number}', params=params, headers=headers)

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

    def update_invoice(self, billing_title_number, invoice_info):
        token = self._get_token(scope_info=False)
        application_key = os.getenv('APPLICATION_KEY')

        headers = {
            'Authorization': token,
            'X-Developer-Application-Key': application_key,
            'Accept': 'application/json',
        }
        response = requests.patch(f'{self.base_url}/boletos/{billing_title_number}', data=json.dumps(invoice_info), headers=headers)

        return response.content


if __name__ == '__main__':
    invoice = {
        "numeroConvenio": 3128557,
        "numeroCarteira": 17,
        "numeroVariacaoCarteira": 35,
        "codigoModalidade": 1,
        "dataEmissao": '.'.join(reversed(str(date.today()).split('-'))),
        "dataVencimento": '.'.join(reversed(str(date.today() + timedelta(days=60)).split('-'))),
        "valorOriginal": 123.45,
        "valorAbatimento": 12.34,
        "quantidadeDiasProtesto": 0,
        "quantidadeDiasNegativacao": 5,
        "orgaoNegativador": 10,
        "indicadorAceiteTituloVencido": "S",
        "numeroDiasLimiteRecebimento": 30,
        "codigoAceite": "N",
        "codigoTipoTitulo": 2,
        "descricaoTipoTitulo": "DM",
        "indicadorPermissaoRecebimentoParcial": "S",
        "numeroTituloBeneficiario": "2A584SDGTE8JN2G",
        "numeroTituloCliente": "00031285570689531501",
        "desconto": {
            "tipo": 2,
            "dataExpiracao": '.'.join(reversed(str(date.today() + timedelta(days=10)).split('-'))),
            "porcentagem": 5.0
        },
        "jurosMora": {
            "tipo": 2,
            "porcentagem": 1.00
        },
        "multa": {
            "tipo": 1,
            "data": '.'.join(reversed(str(date.today() + timedelta(days=65)).split('-'))),
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
        "indicadorPix": "N",
        "segundoDesconto": {
            "dataExpiracao": '.'.join(reversed(str(date.today() + timedelta(days=30)).split('-'))),
            "porcentagem": 4.0
        },
        "terceiroDesconto": {
            "dataExpiracao": '.'.join(reversed(str(date.today() + timedelta(days=50)).split('-'))),
            "porcentagem": 3.0
        },
    }

    invoice_2 = {
        "numeroConvenio": 3128557,
        "indicadorNovaDataVencimento": "N",
        "alteracaoData": {
        "novaDataVencimento": '.'.join(reversed(str(date.today() + timedelta(days=55)).split('-')))
        },
        "indicadorAtribuirDesconto": "S",
        "desconto": {
        "tipoPrimeiroDesconto": 1,
        "valorPrimeiroDesconto": 5,
        "dataPrimeiroDesconto": '.'.join(reversed(str(date.today() + timedelta(days=10)).split('-'))),
        "tipoSegundoDesconto": 1,
        "valorSegundoDesconto": 4,
        "dataSegundoDesconto": '.'.join(reversed(str(date.today() + timedelta(days=30)).split('-'))),
        "tipoTerceiroDesconto": 1,
        "valorTerceiroDesconto": 3,
        "dataTerceiroDesconto": '.'.join(reversed(str(date.today() + timedelta(days=50)).split('-')))
        },
        "indicadorAlterarDesconto": "S",
        "alteracaoDesconto": {
        "tipoPrimeiroDesconto": 1,
        "novoValorPrimeiroDesconto": 20,
        "novaDataLimitePrimeiroDesconto": '.'.join(reversed(str(date.today() + timedelta(days=10)).split('-'))),
        "tipoSegundoDesconto": 1,
        "novoValorSegundoDesconto": 10,
        "novaDataLimiteSegundoDesconto": '.'.join(reversed(str(date.today() + timedelta(days=30)).split('-'))),
        "tipoTerceiroDesconto": 1,
        "novoValorTerceiroDesconto": 5,
        "novaDataLimiteTerceiroDesconto": '.'.join(reversed(str(date.today() + timedelta(days=45)).split('-'))),
        },
        "indicadorAlterarDataDesconto": "S",
        "alteracaoDataDesconto": {
        "novaDataLimitePrimeiroDesconto": '.'.join(reversed(str(date.today() + timedelta(days=20)).split('-'))),
        "novaDataLimiteSegundoDesconto": '.'.join(reversed(str(date.today() + timedelta(days=40)).split('-'))),
        "novaDataLimiteTerceiroDesconto": '.'.join(reversed(str(date.today() + timedelta(days=60)).split('-'))),
        },
        "indicadorProtestar": "N",
        "protesto": {
            "quantidadeDiasProtesto": 0
        },
        "indicadorSustacaoProtesto": "N",
        "indicadorCancelarProtesto": "S",
        "indicadorIncluirAbatimento": "S",
        "abatimento": {
            "valorAbatimento": 12.34
        },
        "indicadorAlterarAbatimento": "S",
        "alteracaoAbatimento": {
            "novoValorAbatimento": 10
        },
        "indicadorCobrarJuros": "S",
        "juros": {
            "tipoJuros": 2,
            "taxaJuros": 10
        },
        "indicadorDispensarJuros": "N",
        "indicadorCobrarMulta": "S",
        "multa": {
            "tipoMulta": 1,
            "valorMulta": 10.00,
            "dataInicioMulta": '.'.join(reversed(str(date.today() + timedelta(days=60)).split('-'))),
            "taxaMulta": 10.00
        },
        "indicadorDispensarMulta": "N",
        "indicadorNegativar": "S",
        "negativacao": {
            "quantidadeDiasNegativacao": 15,
            "tipoNegativacao": 1
        },
        "indicadorAlterarSeuNumero": "S",
        "alteracaoSeuNumero": {
            "codigoSeuNumero": "BA695S1GTE8JN2A"
        },
        "indicadorAlterarEnderecoPagador": "S",
        "alteracaoEndereco": {
            "enderecoPagador": "Avenida São Cristovão",
            "bairroPagador": "Centro",
            "cidadePagador": "Sucupira",
            "UFPagador": "TO",
            "CEPPagador": 77458000
        },
        "indicadorAlterarPrazoBoletoVencido": "S",
        "alteracaoPrazo": {
            "quantidadeDiasAceite": 30
        }
    }

    bb_charging_api = BBChargingAPI(test_environment=True)
    # print(bb_charging_api.get_invoices('A', 452, 123873))
    # print(bb_charging_api.register_invoice(invoice))
    print(bb_charging_api.get_invoice('3128557', '00031285570689531501'))
    print(bb_charging_api.update_invoice('00031285570689531501', invoice_2))
