# 🔹 6️⃣ Bank Transaction Validator

def withdraw(balance, amount):
    if amount <= 0:
        return "invalid Amount"
    elif amount > balance:
        return "Insufficient balance"
    else:
        balance -= amount
        return f"withdrawl Successful! Remaining Balance: {balance}"

print(withdraw(1000, 1200))
print(withdraw(2000, 1500))