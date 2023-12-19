import re

class CustomException(Exception):
    pass


def StringCheck(var):
    for i in var:
        if i.isalpha() or i.isspace():
            pass
        else:
            raise CustomException("Should contain only letters")


def validate_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo\.com)$')
    if not email_pattern.match(email):
        raise CustomException("should end with @gmail/@yahoo.com")


def validate_phone(Phone):
    for i in Phone:
        if i.isdigit():
            pass
        else:
            raise CustomException("should contain only numbers")
