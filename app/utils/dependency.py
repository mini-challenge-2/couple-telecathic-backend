import random
import string
import time
import jwt

def generate_uuid(length=8):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_jwt_token(key_id: str, team_id: str, private_key: str):
    headers = {
        "alg": "ES256",
        "kid": key_id
    }
    payload = {
        "iss": team_id,
        "iat": int(time.time())
    }
    token = jwt.encode(payload, private_key, algorithm="ES256", headers=headers)
    return token
