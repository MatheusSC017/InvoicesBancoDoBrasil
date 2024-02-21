class Invoice:
    @property
    def numeroConvenio(self):
        return self._numeroConvenio

    @property
    def numeroCarteira(self):
        return self._numeroCarteira

    @property
    def numeroVariacaoCarteira(self):
        return self._numeroVariacaoCarteira

    @property
    def codigoModalidade(self):
        return self._codigoModalidade

    @property
    def dataEmissao(self):
        return self._dataEmissao

    @property
    def dataVencimento(self):
        return self._dataVencimento

    @property
    def valorOriginal(self):
        return self._valorOriginal

    @property
    def valorAbatimento(self):
        return self._valorAbatimento

    @property
    def quantidadeDiasProtesto(self):
        return self._quantidadeDiasProtesto

    @property
    def quantidadeDiasNegativacao(self):
        return self._quantidadeDiasNegativacao

    @property
    def orgaoNegativador(self):
        return self._orgaoNegativador

    @property
    def indicadorAceiteTituloVencido(self):
        return self._indicadorAceiteTituloVencido

    @property
    def numeroDiasLimiteRecebimento(self):
        return self._numeroDiasLimiteRecebimento

    @property
    def codigoAceite(self):
        return self._codigoAceite

    @property
    def codigoTipoTitulo(self):
        return self._codigoTipoTitulo

    @property
    def descricaoTipoTitulo(self):
        return self._descricaoTipoTitulo

    @property
    def indicadorPermissaoRecebimentoParcial(self):
        return self._indicadorPermissaoRecebimentoParcial

    @property
    def numeroTituloBeneficiario(self):
        return self._numeroTituloBeneficiario

    @property
    def numeroTituloCliente(self):
        return self._numeroTituloCliente

    @property
    def desconto(self):
        return self._desconto

    @property
    def segundoDesconto(self):
        return self._segundoDesconto

    @property
    def terceiroDesconto(self):
        return self._terceiroDesconto

    @property
    def jurosMora(self):
        return self._jurosMora

    @property
    def multa(self):
        return self._multa

    @property
    def pagador(self):
        return self._pagador

    @property
    def beneficiarioFinal(self):
        return self._beneficiarioFinal

    @property
    def indicadorPix(self):
        return self._indicadorPix

    @numeroConvenio.setter
    def numeroConvenio(self, value):
        self._numeroConvenio = value

    @numeroCarteira.setter
    def numeroCarteira(self, value):
        self._numeroCarteira = value

    @numeroVariacaoCarteira.setter
    def numeroVariacaoCarteira(self, value):
        self._numeroVariacaoCarteira = value

    @codigoModalidade.setter
    def codigoModalidade(self, value):
        self._codigoModalidade = value

    @dataEmissao.setter
    def dataEmissao(self, value):
        self._dataEmissao = value

    @dataVencimento.setter
    def dataVencimento(self, value):
        self._dataVencimento = value

    @valorOriginal.setter
    def valorOriginal(self, value):
        self._valorOriginal = value

    @valorAbatimento.setter
    def valorAbatimento(self, value):
        self._valorAbatimento = value

    @quantidadeDiasProtesto.setter
    def quantidadeDiasProtesto(self, value):
        self._quantidadeDiasProtesto = value

    @quantidadeDiasNegativacao.setter
    def quantidadeDiasNegativacao(self, value):
        self._quantidadeDiasNegativacao = value

    @orgaoNegativador.setter
    def orgaoNegativador(self, value):
        self._orgaoNegativador = value

    @indicadorAceiteTituloVencido.setter
    def indicadorAceiteTituloVencido(self, value):
        self._indicadorAceiteTituloVencido = value

    @numeroDiasLimiteRecebimento.setter
    def numeroDiasLimiteRecebimento(self, value):
        self._numeroDiasLimiteRecebimento = value

    @codigoAceite.setter
    def codigoAceite(self, value):
        self._codigoAceite = value

    @codigoTipoTitulo.setter
    def codigoTipoTitulo(self, value):
        self._codigoTipoTitulo = value

    @descricaoTipoTitulo.setter
    def descricaoTipoTitulo(self, value):
        self._descricaoTipoTitulo = value

    @indicadorPermissaoRecebimentoParcial.setter
    def indicadorPermissaoRecebimentoParcial(self, value):
        self._indicadorPermissaoRecebimentoParcial = value

    @numeroTituloBeneficiario.setter
    def numeroTituloBeneficiario(self, value):
        self._numeroTituloBeneficiario = value

    @numeroTituloCliente.setter
    def numeroTituloCliente(self, value):
        self._numeroTituloCliente = value

    @desconto.setter
    def desconto(self, value):
        self._desconto = value

    @segundoDesconto.setter
    def segundoDesconto(self, value):
        self._segundoDesconto = value

    @terceiroDesconto.setter
    def terceiroDesconto(self, value):
        self._terceiroDesconto = value

    @jurosMora.setter
    def jurosMora(self, value):
        self._jurosMora = value

    @multa.setter
    def multa(self, value):
        self._multa = value

    @pagador.setter
    def pagador(self, value):
        self._pagador = value

    @beneficiarioFinal.setter
    def beneficiarioFinal(self, value):
        self._beneficiarioFinal = value

    @indicadorPix.setter
    def indicadorPix(self, value):
        self._indicadorPix = value

    def to_dict(self):
        result = {
            "numeroConvenio": self.numeroConvenio,
            "numeroCarteira": self.numeroCarteira,
            "numeroVariacaoCarteira": self.numeroVariacaoCarteira,
            "codigoModalidade": self.codigoModalidade,
            "dataEmissao": self.dataEmissao,
            "dataVencimento": self.dataVencimento,
            "valorOriginal": self.valorOriginal,
            "valorAbatimento": self.valorAbatimento,
            "quantidadeDiasProtesto": self.quantidadeDiasProtesto,
            "quantidadeDiasNegativacao": self.quantidadeDiasNegativacao,
            "orgaoNegativador": self.orgaoNegativador,
            "indicadorAceiteTituloVencido": self.indicadorAceiteTituloVencido,
            "numeroDiasLimiteRecebimento": self.numeroDiasLimiteRecebimento,
            "codigoAceite": self.codigoAceite,
            "codigoTipoTitulo": self.codigoTipoTitulo,
            "descricaoTipoTitulo": self.descricaoTipoTitulo,
            "indicadorPermissaoRecebimentoParcial": self.indicadorPermissaoRecebimentoParcial,
            "numeroTituloBeneficiario": self.numeroTituloBeneficiario,
            "numeroTituloCliente": self.numeroTituloCliente,
            "desconto": self.desconto,
            "segundoDesconto": self.segundoDesconto,
            "terceiroDesconto": self.terceiroDesconto,
            "jurosMora": self.jurosMora,
            "multa": self.multa,
            "pagador": self.pagador,
            "beneficiarioFinal": self.beneficiarioFinal,
            "indicadorPix": self.indicadorPix
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

    invoice_instance.numeroConvenio = 3128557
    invoice_instance.numeroCarteira = 17
    invoice_instance.numeroVariacaoCarteira = 35
    invoice_instance.codigoModalidade = 1
    invoice_instance.dataEmissao = "15.02.2024"
    invoice_instance.dataVencimento = "31.03.2024"
    invoice_instance.valorOriginal = 123.45
    invoice_instance.valorAbatimento = 12.34
    invoice_instance.quantidadeDiasProtesto = 0
    invoice_instance.quantidadeDiasNegativacao = 0
    invoice_instance.orgaoNegativador = 10
    invoice_instance.indicadorAceiteTituloVencido = "S"
    invoice_instance.numeroDiasLimiteRecebimento = 1
    invoice_instance.codigoAceite = "N"
    invoice_instance.codigoTipoTitulo = 2
    invoice_instance.descricaoTipoTitulo = "DM"
    invoice_instance.indicadorPermissaoRecebimentoParcial = "S"
    invoice_instance.numeroTituloBeneficiario = "2A584SDGTE8JN2G"
    invoice_instance.numeroTituloCliente = "00031285570689531552"
    invoice_instance.desconto = {
        "tipo": 2,
        "dataExpiracao": "28.02.2024",
        "porcentagem": 5
    }
    invoice_instance.segundoDesconto = {
        "dataExpiracao": "10.03.2024",
        "porcentagem": 4
    }
    invoice_instance.terceiroDesconto = {
        "dataExpiracao": "20.03.2024",
        "porcentagem": 3
    }
    invoice_instance.jurosMora = {
        "tipo": 2,
        "porcentagem": 1.00
    }
    invoice_instance.multa = {
        "tipo": 1,
        "data": "01.04.2024",
        "valor": 10.00
    }
    invoice_instance.pagador = {
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
    invoice_instance.beneficiarioFinal = {
        "tipoInscricao": 2,
        "numeroInscricao": 74910037000193,
        "nome": "Dirceu Borboleta"
    }
    invoice_instance.indicadorPix = "N"

    print(invoice_instance.to_dict() == invoice)
