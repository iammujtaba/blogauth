import secrets
from django.core.signing import Signer


def generate_hex_token(size: int=10)->str:
    return secrets.token_urlsafe(size)

def generate_signed_token(base_token:str)->str:
    return Signer().sign(base_token)

def get_original_unsigned_token(token:str)->str:
    return Signer().unsign(token)

def generate_access_refresh_token() -> str:
    return generate_signed_token(generate_hex_token(14)),generate_signed_token(generate_hex_token(14))