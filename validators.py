import re


def validate_date(date):
    return True if re.search(r"^\d{4}-\d{2}-\d{2}$", date) is not None else False


def validate_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    digit1 = 11 - (total % 11)
    digit1 = digit1 if digit1 < 10 else 0

    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    digit2 = 11 - (total % 11)
    digit2 = digit2 if digit2 < 10 else 0

    if int(cpf[9]) == digit1 and int(cpf[10]) == digit2:
        return True
    else:
        return False


def validate_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))

    if len(cnpj) != 14:
        return False

    total = 0
    weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(12):
        total += int(cnpj[i]) * weights[i]
    digit1 = 11 - (total % 11)
    digit1 = digit1 if digit1 < 10 else 0

    total = 0
    weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(13):
        total += int(cnpj[i]) * weights[i]
    digit2 = 11 - (total % 11)
    digit2 = digit2 if digit2 < 10 else 0

    if int(cnpj[12]) == digit1 and int(cnpj[13]) == digit2:
        return True
    else:
        return False
