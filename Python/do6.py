# 9️⃣ Unique Username Generator

def generate_username(name, existing_users):
    base = name.lower().replace(" ", ".")
    counter = 1
    username = base
    while username in existing_users:
        username = f"{base}{counter}"
        counter += 1
    return username

print(generate_username("Alpha Glaxy", ["alphaglaxy", "alphaglaxy1"]))