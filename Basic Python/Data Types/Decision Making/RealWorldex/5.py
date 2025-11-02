# 🔹 3️⃣ Discount Calculator (E-commerce App)

def calculate_discount(amount):
    if amount >= 5000:
        discount = 0.2
    elif amount >= 2000:
        discount = 0.1
    else:
        discount = 0.5
    return f"Discount: {amount * discount}"

print(calculate_discount(7000))
print(calculate_discount(1500))