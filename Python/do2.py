# 2️⃣ Password Strength Checker
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: too short"
    if not any(ch.isdigit() for ch in password):
        return "Weak: must contain number"
    if not any(ch.isupper() for ch in password):
        return "Weak: must contain uppercase"
    return "Strong"

print(check_password_strength("Abhi1234"))
