import re
from rest_framework.exceptions import ValidationError

def _is_strong_password(password):
    # Check if password has at least 8 characters
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    # Check if password has at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must have at least one uppercase letter.")

    # Check if password has at least one lowercase letter
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must have at least one lowercase letter.")

    # Check if password has at least one digit
    if not re.search(r'\d', password):
        raise ValidationError("Password must have at least one digit.")

    # Check if password has at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError("Password must have at least one special character.")
    return True

def is_strong_password(password,raise_exception=False):
    try:
        return _is_strong_password(password)
    except Exception as e:
        if raise_exception:
            raise e
        return False
