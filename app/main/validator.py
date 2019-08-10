import re


def validate_not_empty(value: str) -> str:
    if not value:
        raise ValueError('value can not be empty')
    return value


def validate_username(value: str) -> str:
    validate_not_empty(value)
    if re.match("(.*?)@.(.*?)") is None:
        raise ValueError('username must be in email type')
    return value
