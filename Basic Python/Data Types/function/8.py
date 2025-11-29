import random

def otp_genrator():
    return random.randint(100000, 999999)

print(otp_genrator())