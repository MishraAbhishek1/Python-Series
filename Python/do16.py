# 17️⃣ Data Encryption / Decryption

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(b"Sensitive Data")
print("Encrypted:", token)
print("Decrypted:", f.decrypt(token))