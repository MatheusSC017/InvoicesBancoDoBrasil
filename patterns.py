def date_pattern(date):
    formatted_date = ''.join(filter(str.isdigit, date))
    return f"{formatted_date[6:]}.{formatted_date[4:6]}.{formatted_date[:4]}"


def value_pattern(value):
    return round(value, 2)


def percentage_pattern(percentage):
    return percentage * 100


def default_pattern(value):
    return value
