import secrets

download_tokens = {}


def generate_token(slug):
    token = secrets.token_urlsafe(32)
    download_tokens[token] = slug
    return token


def validate_token(token):
    return download_tokens.get(token)