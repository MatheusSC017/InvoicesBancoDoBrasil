from patterns import *

from validators import validate_date

TITLE_TYPE_CODE_OPTIONS = {
    1: 'CHEQUE',
    2: 'DUPLICATA MERCANTIL',
    3: 'DUPLICATA MTIL POR INDICACAO',
    4: 'DUPLICATA DE SERVICO',
    5: 'DUPLICATA DE SRVC P/INDICACAO',
    6: 'DUPLICATA RURAL',
    7: 'LETRA DE CAMBIO',
    8: 'NOTA DE CREDITO COMERCIAL',
    9: 'NOTA DE CREDITO A EXPORTACAO',
    10: 'NOTA DE CREDITO INDULTRIAL',
    11: 'NOTA DE CREDITO RURAL',
    12: 'NOTA PROMISSORIA',
    13: 'NOTA PROMISSORIA RURAL',
    14: 'TRIPLICATA MERCANTIL',
    15: 'TRIPLICATA DE SERVICO',
    16: 'NOTA DE SEGURO',
    17: 'RECIBO',
    18: 'FATURA',
    19: 'NOTA DE DEBITO',
    20: 'APOLICE DE SEGURO',
    21: 'MENSALIDADE ESCOLAR',
    22: 'PARCELA DE CONSORCIO',
    23: 'DIVIDA ATIVA DA UNIAO',
    24: 'DIVIDA ATIVA DE ESTADO',
    25: 'DIVIDA ATIVA DE MUNICIPIO',
    31: 'CARTAO DE CREDITO',
    32: 'BOLETO PROPOSTA',
    33: 'BOLETO APORTE',
    99: 'OUTROS'
}

FIELDS = {
    "type": "tipo",
    "value": "valor",
    "percentage": "porcentagem",
    "expiration_date": "dataExpiracao",
    "date": "data",
}

FIELDS_FORMATATION = {
    "type": default_pattern,
    "value": value_pattern,
    "percentage": percentage_pattern,
    "expiration_date": date_pattern,
    "date": date_pattern,
}


class Invoice:
    def __init__(self):
        self._agreement_number = None
        self._wallet_number = None
        self._wallet_variation_number = None
        self._modality_code = None
        self._issue_date = None
        self._expiration_date = None
        self._original_value = 0
        self._rebate_value = 0
        self._number_of_protest_days = 0
        self._number_of_days_to_negative = 0
        self._negative_organ = 0
        self._indicator_accepts_expired_title = False
        self._number_of_days_receiving_deadline = 0
        self._accept_code = False
        self._title_type_code = 0
        self._description_type_title = ""
        self._partial_receipt_permission_indicator = False
        self._beneficiary_title_number = ""
        self._customer_title_number = ""
        self._discount = {"type": 0}
        self._second_discount = None
        self._third_discount = None
        self._late_payment_interest = None
        self._fine = None
        self._payer = None
        self._final_beneficiary = None
        self._pix_indicator = False

    @property
    def agreement_number(self):
        """ numeroConvenio """
        return self._agreement_number

    @property
    def wallet_number(self):
        """ numeroCarteira """
        return self._wallet_number

    @property
    def wallet_variation_number(self):
        """ numeroVariacaoCarteira """
        return self._wallet_variation_number

    @property
    def modality_code(self):
        """ codigoModalidade """
        return self._modality_code

    @property
    def issue_date(self):
        """ dataEmissao """
        return date_pattern(self._issue_date)

    @property
    def expiration_date(self):
        return date_pattern(self._expiration_date)

    @property
    def original_value(self):
        """ valorOriginal """
        if self._original_value <= 0:
            raise ValueError("The original value must be greater than zero, define the bill value")
        return value_pattern(self._original_value)

    @property
    def rebate_value(self):
        return value_pattern(self._rebate_value)

    @property
    def number_of_protest_days(self):
        """ quantidadeDiasProtesto """
        return self._number_of_protest_days

    @property
    def number_of_days_to_negative(self):
        """ quantidadeDiasNegativacao """
        return self._number_of_days_to_negative

    @property
    def negative_organ(self):
        """ orgaoNegativador """
        return self._negative_organ

    @property
    def indicator_accepts_expired_title(self):
        """ indicadorAceiteTituloVencido """
        return "S" if self._indicator_accepts_expired_title else "N"

    @property
    def number_of_days_receiving_deadline(self):
        """ numeroDiasLimiteRecebimento """
        return self._number_of_days_receiving_deadline

    @property
    def accept_code(self):
        """ codigoAceite """
        return "S" if self._accept_code else "N"

    @property
    def title_type_code(self):
        """ codigoTipoTitulo """
        return self._title_type_code

    @property
    def description_type_title(self):
        """ descricaoTipoTitulo """
        return self._description_type_title

    @property
    def partial_receipt_permission_indicator(self):
        """ indicadorPermissaoRecebimentoParcial """
        return "S" if self._partial_receipt_permission_indicator else "N"

    @property
    def beneficiary_title_number(self):
        """ numeroTituloBeneficiario """
        return self._beneficiary_title_number

    @property
    def customer_title_number(self):
        """ numeroTituloCliente """
        if self._agreement_number is None:
            raise ValueError("You must define the agreement number before")
        return f"000{self._agreement_number}{self._customer_title_number}"

    @property
    def discount(self):
        """ desconto """
        return {FIELDS[key]: FIELDS_FORMATATION[key](self._discount[key]) for key in self._discount.keys()}

    @property
    def discount_value(self):
        """ desconto """
        if self._discount['type'] == 0:
            return 0
        elif self._discount['type'] == 1:
            return self._discount['value']
        else:
            return self._discount['percentage'] * self._original_value

    @property
    def second_discount(self):
        """ segundoDesconto """
        return {FIELDS[key]: FIELDS_FORMATATION[key](self._second_discount[key])
                for key in self._second_discount.keys()}

    @property
    def third_discount(self):
        """ terceiroDesconto """
        return {FIELDS[key]: FIELDS_FORMATATION[key](self._third_discount[key]) for key in self._third_discount.keys()}

    @property
    def late_payment_interest(self):
        """ jurosMora """
        return {FIELDS[key]: FIELDS_FORMATATION[key](self._late_payment_interest[key])
                for key in self._late_payment_interest.keys()}

    @property
    def fine(self):
        """ multa """
        return {FIELDS[key]: FIELDS_FORMATATION[key](self._fine[key]) for key in self._fine.keys()}

    @property
    def payer(self):
        """ pagador """
        return self._payer

    @property
    def final_beneficiary(self):
        """ beneficiarioFinal """
        return self._final_beneficiary

    @property
    def pix_indicator(self):
        """ indicadorPix """
        return "S" if self._pix_indicator else "N"

    @agreement_number.setter
    def agreement_number(self, value):
        """ numeroConvenio """
        if not isinstance(value, int) or not(1000000 <= value <= 9999999):
            raise ValueError("For the contract number only a 7-digit number will be accepted")
        self._agreement_number = value

    @wallet_number.setter
    def wallet_number(self, value):
        """ numeroCarteira """
        if not isinstance(value, int):
            raise ValueError("Wallet number only accepts number values")
        self._wallet_number = value

    @wallet_variation_number.setter
    def wallet_variation_number(self, value):
        """ numeroVariacaoCarteira """
        if not isinstance(value, int):
            raise ValueError("Wallet variation number only accepts number values")
        self._wallet_variation_number = value

    @modality_code.setter
    def modality_code(self, value):
        """ codigoModalidade """
        if value != 1 and value != 4:
            raise ValueError("Modality code only accepts the numbers 1 and 4")
        self._modality_code = value

    @issue_date.setter
    def issue_date(self, value):
        """ dataEmissao """
        if not validate_date(value):
            raise ValueError("Error when defining the issue date, for date type fields use the international format")
        self._issue_date = value

    @expiration_date.setter
    def expiration_date(self, value):
        """ dataVencimento """
        if not validate_date(value):
            raise ValueError("Error when defining the expiration date, "
                             "for date type fields use the international format")
        self._expiration_date = value

    @original_value.setter
    def original_value(self, value):
        """ valorOriginal """
        if (self._discount['type'] != 2 and value < self.rebate_value + self.discount_value) or \
           (self._discount['type'] == 2 and value < self.rebate_value + (self._discount['percentage'] * value)):
            raise ValueError("Invoice value in the register must be greater than the sum of the fields “rebate_value” "
                             "and “discount”")
        self._original_value = value

    @rebate_value.setter
    def rebate_value(self, value):
        """ valorAbatimento """
        if value < 0.0:
            raise ValueError("The rebate amount must be greater than or equal to zero")
        self._rebate_value = value

    @number_of_protest_days.setter
    def number_of_protest_days(self, value):
        """ quantidadeDiasProtesto """
        if value < 0.0:
            raise ValueError("The number of protest days must be greater than or equal to zero")
        if (value < 3 or value > 29) and value not in [0, 35, 40, 45]:
            raise ValueError("The number of protest days must be 3 to 5 business days or "
                             "6 to 29, 35, 40 or 45 calendar days")

        self._number_of_protest_days = value

    @number_of_days_to_negative.setter
    def number_of_days_to_negative(self, value):
        """ quantidadeDiasNegativacao """
        if value < 0.0:
            raise ValueError("The number of days to negative must be greater than or equal to zero")
        self._number_of_days_to_negative = value

    @negative_organ.setter
    def negative_organ(self, value):
        """ orgaoNegativador """
        if value != 10 and value != 11:
            raise ValueError("Error when defining the negative organ, choose a domain between 10 - SERASA; 11 - QUOD")
        self._negative_organ = value

    @indicator_accepts_expired_title.setter
    def indicator_accepts_expired_title(self, value):
        """ indicadorAceiteTituloVencido """
        if not isinstance(value, bool):
            raise TypeError("Only boolean values are accepted to indicator accepts expired title")
        self._indicator_accepts_expired_title = value

    @number_of_days_receiving_deadline.setter
    def number_of_days_receiving_deadline(self, value):
        """ numeroDiasLimiteRecebimento """
        if value < 0.0:
            raise ValueError("The number of days receiving deadline must be greater than or equal to zero")
        self._number_of_days_receiving_deadline = value

    @accept_code.setter
    def accept_code(self, value):
        """ codigoAceite """
        if not isinstance(value, bool):
            raise TypeError("Only boolean values are accepted to accept code")
        self._accept_code = value

    @title_type_code.setter
    def title_type_code(self, value):
        """ codigoTipoTitulo """
        if value not in TITLE_TYPE_CODE_OPTIONS.keys():
            raise ValueError(f"Only the next values are accepted: {TITLE_TYPE_CODE_OPTIONS}")
        self._title_type_code = value

    @description_type_title.setter
    def description_type_title(self, value):
        """ descricaoTipoTitulo """
        self._description_type_title = value

    @partial_receipt_permission_indicator.setter
    def partial_receipt_permission_indicator(self, value):
        """ indicadorPermissaoRecebimentoParcial """
        if not isinstance(value, bool):
            raise TypeError("Only boolean values are accepted to partial_receipt_permission_indicator")
        self._partial_receipt_permission_indicator = value

    @beneficiary_title_number.setter
    def beneficiary_title_number(self, value):
        """ numeroTituloBeneficiario """
        if len(value) > 15:
            raise ValueError("the beneficiary's title number must be less than 15 characters")
        self._beneficiary_title_number = value

    @customer_title_number.setter
    def customer_title_number(self, value):
        """ numeroTituloCliente """
        if len(value) != 10:
            raise ValueError("Please enter only the last 10 digits of the customer's title number, as the first 10 "
                             "will be filled in automatically following the pattern: 000 + agreement number (7 digits) "
                             "+ control number (10 digits).")
        self._customer_title_number = value

    @discount.setter
    def discount(self, data):
        """ desconto """
        if 'type' not in data.keys() or data['type'] not in [0, 1, 2, ]:
            raise ValueError("Invalid type, choose between the options: 0 - No discount; 1 - Fixed value until the "
                             "informed date; 2 - percentage up to the informed date.")

        self._discount = {'type': data['type'], }
        if data['type'] != 0:
            if 'expiration_date' not in data.keys() or not validate_date(data['expiration_date']):
                raise ValueError("Error when defining the discount date, "
                                 "for date type fields use the international format")
            self._discount['expiration_date'] = data['expiration_date']

            if data['type'] == 1:
                if 'value' not in data.keys() or data['value'] > self._original_value - self.rebate_value:
                    raise ValueError("Invoice value in the register must be greater than the sum of the fields "
                                     "“rebate_value” and “discount”")
                self._discount['value'] = data['value']
            else:
                if 'percentage' not in data.keys() or data['percentage'] >= 1 or data['percentage'] == 0:
                    raise ValueError("The percentage must be a number between 0 and 1")
                if (data['percentage'] * self._original_value) > self._original_value - self.rebate_value:
                    raise ValueError("Invoice value in the register must be greater than the sum of the fields "
                                     "“rebate_value” and “discount”")
                self._discount['percentage'] = data['percentage']

    @second_discount.setter
    def second_discount(self, data):
        """ segundoDesconto """
        if self._discount is None or self._discount['type'] == 0:
            raise ValueError("To define the second discount you must configure the first discount, with a type other "
                             "than 0")

        if 'expiration_date' not in data.keys() or not validate_date(data['expiration_date']):
            raise ValueError("The expiration date is required, for date type fields use the international format")
        self._second_discount = {'expiration_date': data['expiration_date']}

        if self._discount['type'] == 1:
            if 'value' not in data.keys() or data['value'] >= self._discount['value']:
                raise ValueError("The value of the second discount must be lower than the first")
            self._second_discount['value'] = data['value']
        else:
            if 'percentage' not in data.keys() or data['percentage'] >= 1 or data['percentage'] == 0:
                raise ValueError("The percentage must be a number between 0 and 1")
            if data['percentage'] >= self._discount['percentage']:
                raise ValueError("The percentage of the second discount must be lower than the first")
            self._second_discount['percentage'] = data['percentage']

    @third_discount.setter
    def third_discount(self, data):
        """ terceiroDesconto """
        if self._discount is None or self._discount['type'] == 0:
            raise ValueError("To define the third discount you must configure the first discount, with a type other "
                             "than 0")

        if self._second_discount is None:
            raise ValueError("To define the third discount you must configure the second discount")

        if 'expiration_date' not in data.keys() or not validate_date(data['expiration_date']):
            raise ValueError("The expiration date is required, for date type fields use the international format")
        self._third_discount = {'expiration_date': data['expiration_date']}

        if self._discount['type'] == 1:
            if 'value' not in data.keys() or data['value'] >= self._second_discount['value']:
                raise ValueError("The value of the third discount must be lower than the second")
            self._third_discount['value'] = data['value']
        else:
            if 'percentage' not in data.keys() or data['percentage'] >= 1 or data['percentage'] == 0:
                raise ValueError("The percentage must be a number between 0 and 1")
            if data['percentage'] >= self._second_discount['percentage']:
                raise ValueError("The percentage of the value discount must be lower than the second")
            self._third_discount['percentage'] = data['percentage']

    @late_payment_interest.setter
    def late_payment_interest(self, data):
        """ jurosMora """
        if 'type' not in data.keys() or data['type'] not in [0, 1, 2, 3]:
            raise ValueError("Invalid type, choose between the options: 0 - Dismiss; 1 - Fixed amount per day of "
                             "delay; 2 - Monthly fee; 3 - Exempt.")

        self._late_payment_interest = {'type': data['type']}

        if data['type'] == 1:
            if 'value' not in data.keys():
                raise ValueError("For this type of interest, enter the fixed daily amount")
            self._late_payment_interest['value'] = data['value']
        elif data['type'] == 2:
            if 'percentage' not in data.keys() or data['percentage'] >= 1 or data['percentage'] == 0:
                raise ValueError("The percentage must be a number between 0 and 1")
            self._late_payment_interest['percentage'] = data['percentage']

    @fine.setter
    def fine(self, data):
        """ multa """
        if 'type' not in data.keys() or data['type'] not in [0, 1, 2, ]:
            raise ValueError("Invalid type, choose between the options: 0 - Dismiss; 1 - Fixed value (from the date "
                             "stipulated in the registration); 2 - Percentage (from the date stipulated in the "
                             "registration).")

        self._fine = {'type': data['type']}

        if 'date' not in data.keys() or not validate_date(data['date']):
            raise ValueError("The date is required, for date type fields use the international format")
        self._fine['date'] = data['date']

        if data['type'] == 1:
            if 'value' not in data.keys():
                raise ValueError("For this type of _fine, enter the fixed daily amount")
            self._fine['value'] = data['value']
        elif data['type'] == 2:
            if 'percentage' not in data.keys() or data['percentage'] >= 1 or data['percentage'] == 0:
                raise ValueError("The percentage must be a number between 0 and 1")
            self._fine['percentage'] = data['percentage']

    @payer.setter
    def payer(self, value):
        """ pagador """
        self._payer = value

    @final_beneficiary.setter
    def final_beneficiary(self, value):
        """ beneficiarioFinal """
        self._final_beneficiary = value

    @pix_indicator.setter
    def pix_indicator(self, value):
        """ indicadorPix """
        if not isinstance(value, bool):
            raise TypeError("Only boolean values are accepted to pix indicator")
        self._pix_indicator = value

    def to_dict(self):
        result = {
            'numeroConvenio': self.agreement_number,
            'numeroCarteira': self.wallet_number,
            'numeroVariacaoCarteira': self.wallet_variation_number,
            'codigoModalidade': self.modality_code,
            'dataEmissao': self.issue_date,
            'dataVencimento': self.expiration_date,
            'valorOriginal': self.original_value,
            'valorAbatimento': self.rebate_value,
            'quantidadeDiasProtesto': self.number_of_protest_days,
            'quantidadeDiasNegativacao': self.number_of_days_to_negative,
            'orgaoNegativador': self.negative_organ,
            'indicadorAceiteTituloVencido': self.indicator_accepts_expired_title,
            'numeroDiasLimiteRecebimento': self.number_of_days_receiving_deadline,
            'codigoAceite': self.accept_code,
            'codigoTipoTitulo': self.title_type_code,
            'descricaoTipoTitulo': self.description_type_title,
            'indicadorPermissaoRecebimentoParcial': self.partial_receipt_permission_indicator,
            'numeroTituloBeneficiario': self.beneficiary_title_number,
            'numeroTituloCliente': self.customer_title_number,
            'desconto': self.discount,
            'jurosMora': self.late_payment_interest,
            'multa': self.fine,
            'pagador': self.payer,
            'beneficiarioFinal': self.final_beneficiary,
            'indicadorPix': self.pix_indicator
        }
        if result['desconto']['tipo'] != 0:
            result['segundoDesconto'] = self.second_discount
            result['terceiroDesconto'] = self.third_discount

        return result


if __name__ == '__main__':
    invoice = {
        "numeroConvenio": 3128557,
        "numeroCarteira": 17,
        "numeroVariacaoCarteira": 35,
        "codigoModalidade": 1,
        "dataEmissao": "15.02.2024",
        "dataVencimento": "31.03.2024",
        "valorOriginal": 123.45,
        "valorAbatimento": 12.34,
        "quantidadeDiasProtesto": 5,
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
            "porcentagem": 5.0
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
        "indicadorPix": "N",
        "segundoDesconto": {
            "dataExpiracao": "10.03.2024",
            "porcentagem": 4.0
        },
        "terceiroDesconto": {
            "dataExpiracao": "20.03.2024",
            "porcentagem": 3.0
        },
    }

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
    invoice_instance.customer_title_number = "0689531552"
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
        "tipoInscricao": 1,
        "numeroInscricao": 97965940132,
        "nome": "Odorico Paraguassu",
        "endereco": "Avenida Dias Gomes 1970",
        "cep": 77458000,
        "cidade": "Sucupira",
        "bairro": "Centro",
        "uf": "TO",
        "telefone": "63987654321"
    }
    invoice_instance.final_beneficiary = {
        "tipoInscricao": 2,
        "numeroInscricao": 74910037000193,
        "nome": "Dirceu Borboleta"
    }
    invoice_instance.pix_indicator = False

    print(invoice_instance.to_dict() == invoice)
    print(invoice)
    print(invoice_instance.to_dict())
