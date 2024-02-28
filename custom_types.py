from enum import Enum


class FieldEnum(Enum):
    TYPE = "tipo"
    VALUE = "valor"
    PERCENTAGE = "porcentagem"
    EXPIRATION_DATE = "dataExpiracao"
    DATE = "data"
    REGISTRATION_TYPE = "tipoInscricao"
    REGISTRATION_NUMBER = "numeroInscricao"
    NAME = "nome"
    ADDRESS = "endereco"
    CEP = "cep"
    CITY = "cidade"
    DISTRICT = "bairro"
    STATE = "uf"
    PHONE = "telefone"


class TitleTypeCode(Enum):
    CHEQUE = 1
    DUPLICATA_MERCANTIL = 2
    DUPLICATA_MTIL_POR_INDICACAO = 3
    DUPLICATA_DE_SERVICO = 4
    DUPLICATA_DE_SRVC_P_INDICACAO = 5
    DUPLICATA_RURAL = 6
    LETRA_DE_CAMBIO = 7
    NOTA_DE_CREDITO_COMERCIAL = 8
    NOTA_DE_CREDITO_A_EXPORTACAO = 9
    NOTA_DE_CREDITO_INDULTRIAL = 10
    NOTA_DE_CREDITO_RURAL = 11
    NOTA_PROMISSORIA = 12
    NOTA_PROMISSORIA_RURAL = 13
    TRIPLICATA_MERCANTIL = 14
    TRIPLICATA_DE_SERVICO = 15
    NOTA_DE_SEGURO = 16
    RECIBO = 17
    FATURA = 18
    NOTA_DE_DEBITO = 19
    APOLICE_DE_SEGURO = 20
    MENSALIDADE_ESCOLAR = 21
    PARCELA_DE_CONSORCIO = 22
    DIVIDA_ATIVA_DA_UNIAO = 23
    DIVIDA_ATIVA_DE_ESTADO = 24
    DIVIDA_ATIVA_DE_MUNICIPIO = 25
    CARTAO_DE_CREDITO = 31
    BOLETO_PROPOSTA = 32
    BOLETO_APORTE = 33
    OUTROS = 99


class DiscountType(Enum):
    NO_DISCOUNT = 0
    FIXED_VALUE = 1
    PERCENTAGE = 2


class LatePaymentType(Enum):
    DISMISS = 0
    FIXED_AMOUNT = 1
    MONTHLY_FEE = 2
    EXEMPT = 3


class Fine(Enum):
    DISMISS = 0
    FIXED_VALUE = 1
    PERCENTAGE = 2


class RegistrationType(Enum):
    CPF = 1
    CNPJ = 2
