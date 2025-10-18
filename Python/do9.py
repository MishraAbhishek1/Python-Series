# 🔟 Token Generator

import secrets

def generate_token(length=16):
    return secrets.token_hex(length)

print("Generated Token:", generate_token())