# 🔹 8️⃣ Electricity Bill Generator

def electricty_bill(units):
    if units <= 100:
        rate = 5
    elif units <= 300:
        rate = 7
    else:
        rate = 10
    
    total = units * rate
    return f"Total Bill : {total}"

print(electricty_bill(250))