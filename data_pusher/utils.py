import random
import string


def generate_user_secret_token(length=64):
    chars = string.ascii_letters + '0123456789'
    token = ''.join(random.choices(chars, k=length))
    return token