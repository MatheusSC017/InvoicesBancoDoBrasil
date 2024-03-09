import json
import ast
import requests
import os
import dotenv
from invoice import Invoice

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

    def get_invoice(self, agreement, billing_title_number, format_json=False):
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

        if format_json:
            return response.content
        else:
            invoice = Invoice()
            response_values = ast.literal_eval(response.content.decode('UTF-8'))
            invoice.load_dict(response_values, agreement, billing_title_number)
            return invoice

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
    invoice_instance = Invoice()

    invoice_instance.agreement_number = 3128557
    invoice_instance.wallet_number = 17
    invoice_instance.wallet_variation_number = 35
    invoice_instance.modality_code = 1
    invoice_instance.issue_date = "2024-02-15"
    invoice_instance.expiration_date = "2024-03-31"
    invoice_instance.original_value = 123.45
    invoice_instance.rebate_value = 12.34
    invoice_instance.number_of_protest_days = 5
    invoice_instance.number_of_days_to_negative = 0
    invoice_instance.negative_organ = 10
    invoice_instance.indicator_accepts_expired_title = True
    invoice_instance.number_of_days_receiving_deadline = 1
    invoice_instance.accept_code = False
    invoice_instance.title_type_code = 2
    invoice_instance.description_type_title = "DM"
    invoice_instance.partial_receipt_permission_indicator = True
    invoice_instance.beneficiary_title_number = "2A584SDGTE8JN2G"
    invoice_instance.customer_title_number = "0689531559"
    invoice_instance.discount = {
        "type": 2,
        "expiration_date": "2024-02-28",
        "percentage": 0.05
    }
    invoice_instance.second_discount = {
        "expiration_date": "2024-03-10",
        "percentage": 0.04
    }
    invoice_instance.third_discount = {
        "expiration_date": "2024-03-20",
        "percentage": 0.03
    }
    invoice_instance.late_payment_interest = {
        "type": 2,
        "percentage": 0.01
    }
    invoice_instance.fine = {
        "type": 1,
        "date": "2024-04-01",
        "value": 10.00
    }
    invoice_instance.payer = {
        "registration_type": 1,
        "registration_number": 97965940132,
        "name": "Odorico Paraguassu",
        "address": "Avenida Dias Gomes 1970",
        "cep": 77458000,
        "city": "Sucupira",
        "district": "Centro",
        "state": "TO",
        "phone": "63987654321"
    }
    invoice_instance.final_beneficiary = {
        "registration_type": 2,
        "registration_number": 74910037000193,
        "name": "Dirceu Borboleta"
    }
    invoice_instance.pix_indicator = False

    bb_charging_api = BBChargingAPI(test_environment=True)
    print(bb_charging_api.get_invoice('3128557', '00031285570689531552').to_dict())
    print(bb_charging_api.get_invoices('A', 452, 123873))
    print(bb_charging_api.register_invoice(invoice_instance.to_dict()))
