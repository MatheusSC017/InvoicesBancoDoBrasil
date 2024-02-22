class Invoice:
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
        return self._issue_date

    @property
    def expiration_date(self):
        return self._expiration_date

    @property
    def original_value(self):
        """ valorOriginal """
        return self._original_value

    @property
    def rebate_value(self):
        return self._rebate_value

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
        return self._indicator_accepts_expired_title

    @property
    def number_of_days_receiving_deadline(self):
        """ numeroDiasLimiteRecebimento """
        return self._number_of_days_receiving_deadline

    @property
    def accept_code(self):
        """ codigoAceite """
        return self._accept_code

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
        return self._partial_receipt_permission_indicator

    @property
    def beneficiary_title_number(self):
        """ numeroTituloBeneficiario """
        return self._beneficiary_title_number

    @property
    def customer_title_number(self):
        """ numeroTituloCliente """
        return self._customer_title_number

    @property
    def discount(self):
        """ desconto """
        return self._discount

    @property
    def second_discount(self):
        """ segundoDesconto """
        return self._second_discount

    @property
    def third_discount(self):
        """ terceiroDesconto """
        return self._third_discount

    @property
    def late_payment_interest(self):
        """ jurosMora """
        return self._late_payment_interest

    @property
    def fine(self):
        """ multa """
        return self._fine

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
        return self._pix_indicator

    @agreement_number.setter
    def agreement_number(self, value):
        """ numeroConvenio """
        self._agreement_number = value

    @wallet_number.setter
    def wallet_number(self, value):
        """ numeroCarteira """
        self._wallet_number = value

    @wallet_variation_number.setter
    def wallet_variation_number(self, value):
        """ numeroVariacaoCarteira """
        self._wallet_variation_number = value

    @modality_code.setter
    def modality_code(self, value):
        """ codigoModalidade """
        self._modality_code = value

    @issue_date.setter
    def issue_date(self, value):
        """ dataEmissao """
        self._issue_date = value

    @expiration_date.setter
    def expiration_date(self, value):
        """ dataVencimento """
        self._expiration_date = value

    @original_value.setter
    def original_value(self, value):
        """ valorOriginal """
        self._original_value = value

    @rebate_value.setter
    def rebate_value(self, value):
        """ valorAbatimento """
        self._rebate_value = value

    @number_of_protest_days.setter
    def number_of_protest_days(self, value):
        """ quantidadeDiasProtesto """
        self._number_of_protest_days = value

    @number_of_days_to_negative.setter
    def number_of_days_to_negative(self, value):
        """ quantidadeDiasNegativacao """
        self._number_of_days_to_negative = value

    @negative_organ.setter
    def negative_organ(self, value):
        """ orgaoNegativador """
        self._negative_organ = value

    @indicator_accepts_expired_title.setter
    def indicator_accepts_expired_title(self, value):
        """ indicadorAceiteTituloVencido """
        self._indicator_accepts_expired_title = value

    @number_of_days_receiving_deadline.setter
    def number_of_days_receiving_deadline(self, value):
        """ numeroDiasLimiteRecebimento """
        self._number_of_days_receiving_deadline = value

    @accept_code.setter
    def accept_code(self, value):
        """ codigoAceite """
        self._accept_code = value

    @title_type_code.setter
    def title_type_code(self, value):
        """ codigoTipoTitulo """
        self._title_type_code = value

    @description_type_title.setter
    def description_type_title(self, value):
        """ descricaoTipoTitulo """
        self._description_type_title = value

    @partial_receipt_permission_indicator.setter
    def partial_receipt_permission_indicator(self, value):
        """ indicadorPermissaoRecebimentoParcial """
        self._partial_receipt_permission_indicator = value

    @beneficiary_title_number.setter
    def beneficiary_title_number(self, value):
        """ numeroTituloBeneficiario """
        self._beneficiary_title_number = value

    @customer_title_number.setter
    def customer_title_number(self, value):
        """ numeroTituloCliente """
        self._customer_title_number = value

    @discount.setter
    def discount(self, value):
        """ desconto """
        self._discount = value

    @second_discount.setter
    def second_discount(self, value):
        """ segundoDesconto """
        self._second_discount = value

    @third_discount.setter
    def third_discount(self, value):
        """ terceiroDesconto """
        self._third_discount = value

    @late_payment_interest.setter
    def late_payment_interest(self, value):
        """ jurosMora """
        self._late_payment_interest = value

    @fine.setter
    def fine(self, value):
        """ multa """
        self._fine = value

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
        self._pix_indicator = value

    def to_dict(self):
        result = {
            "numeroConvenio": self.agreement_number,
            "numeroCarteira": self.wallet_number,
            "numeroVariacaoCarteira": self.wallet_variation_number,
            "codigoModalidade": self.modality_code,
            "dataEmissao": self.issue_date,
            "dataVencimento": self.expiration_date,
            "valorOriginal": self.original_value,
            "valorAbatimento": self.rebate_value,
            "quantidadeDiasProtesto": self.number_of_protest_days,
            "quantidadeDiasNegativacao": self.number_of_days_to_negative,
            "orgaoNegativador": self.negative_organ,
            "indicadorAceiteTituloVencido": self.indicator_accepts_expired_title,
            "numeroDiasLimiteRecebimento": self.number_of_days_receiving_deadline,
            "codigoAceite": self.accept_code,
            "codigoTipoTitulo": self.title_type_code,
            "descricaoTipoTitulo": self.description_type_title,
            "indicadorPermissaoRecebimentoParcial": self.partial_receipt_permission_indicator,
            "numeroTituloBeneficiario": self.beneficiary_title_number,
            "numeroTituloCliente": self.customer_title_number,
            "desconto": self.discount,
            "segundoDesconto": self.second_discount,
            "terceiroDesconto": self.third_discount,
            "jurosMora": self.late_payment_interest,
            "multa": self.fine,
            "pagador": self.payer,
            "beneficiarioFinal": self.final_beneficiary,
            "indicadorPix": self.pix_indicator
        }
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

    invoice_instance = Invoice()

    invoice_instance.agreement_number = 3128557
    invoice_instance.wallet_number = 17
    invoice_instance.wallet_variation_number = 35
    invoice_instance.modality_code = 1
    invoice_instance.issue_date = "15.02.2024"
    invoice_instance.expiration_date = "31.03.2024"
    invoice_instance.original_value = 123.45
    invoice_instance.rebate_value = 12.34
    invoice_instance.number_of_protest_days = 0
    invoice_instance.number_of_days_to_negative = 0
    invoice_instance.negative_organ = 10
    invoice_instance.indicator_accepts_expired_title = "S"
    invoice_instance.number_of_days_receiving_deadline = 1
    invoice_instance.accept_code = "N"
    invoice_instance.title_type_code = 2
    invoice_instance.description_type_title = "DM"
    invoice_instance.partial_receipt_permission_indicator = "S"
    invoice_instance.beneficiary_title_number = "2A584SDGTE8JN2G"
    invoice_instance.customer_title_number = "00031285570689531552"
    invoice_instance.discount = {
        "tipo": 2,
        "dataExpiracao": "28.02.2024",
        "porcentagem": 5
    }
    invoice_instance.second_discount = {
        "dataExpiracao": "10.03.2024",
        "porcentagem": 4
    }
    invoice_instance.third_discount = {
        "dataExpiracao": "20.03.2024",
        "porcentagem": 3
    }
    invoice_instance.late_payment_interest = {
        "tipo": 2,
        "porcentagem": 1.00
    }
    invoice_instance.fine = {
        "tipo": 1,
        "data": "01.04.2024",
        "valor": 10.00
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
    invoice_instance.pix_indicator = "N"

    print(invoice_instance.to_dict() == invoice)
