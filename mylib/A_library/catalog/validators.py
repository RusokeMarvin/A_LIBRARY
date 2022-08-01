from django.core.exceptions import ValidationError
import re

def validate_firstname_length(value):
    length= len(value)
    if length < 2:
        raise ValidationError("The length of the first name must be at least 2 characters in length")
    else:
        return value

def validate_lastname_length(value):
    length= len(value)
    if length < 2:
        raise ValidationError("The length of the last name must be at least 2 characters in length")
    else:
        return value

def validate_username_length(value):
    length= len(value)
    if length < 3 or length > 25:
        raise ValidationError("The length of the username must be between 3 and 25 characters")
    else:
        return value


def validate_username_alphadigits(value):
    validmatch= re.match('^[\w]+$', value)
    if not validmatch:
        raise ValidationError("The username can only contain alphabetical characters and numbers")
    else:
        return value

def validate_password_length(value):
    length= len(value)
    if length < 8 or length > 30:
        raise ValidationError("The password must be at least 8 characters in length and no greater than 30 characters")
    else:
        return value

def validate_password_digit(value):
    if not re.search(r"[\d]+", value):
        raise ValidationError("The password must contain at least one digit")
    else:
        return value

def validate_password_uppercase(value):
    if not re.search(r"[A-Z]+", value):
        raise ValidationError("The password must contain at least one uppercase character")
    else:
        return value


def validate_phonenumber(value):
    regex= r"\(\w{3}\)\w{3}-\w{4}"
    regex2= r"\w{3}-\w{3}-\w{4}"
    regex3= r"\b\w{10,11}\b"
    if not re.search(regex, value) and not re.search(regex2, value) and not re.search(regex3, value):
        raise ValidationError("The phone number must be in format (###)###-###, ###-###-###, ##########, or ########### ")
    else:
        return value  