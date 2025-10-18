# 18️⃣ Email Masking (Privacy)

def mask_email(email):
    name, domain = email.split("@")
    return f"{name[3]} + ***@ + {domain}"

print(mask_email("abhi@gmail.com"))

# ------------------ another way ----------------

def mask_email(email):
    name, domain = email.split("@")
    return name[0] + "***@" + domain

print(mask_email("abhi@gmail.com"))
