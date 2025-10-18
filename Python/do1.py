# 1️⃣ Email Validation (Signup ke time)

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

print(is_valid_email("user@gmail.com"))  # ✅ True
print(is_valid_email("invalid@com"))     # ❌ False
