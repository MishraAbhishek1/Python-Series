# 🔹 5️⃣ Temperature Alert System

def temperature_alert(temp):
    if temp > 40:
        return "High Temperature Alert"
    elif temp < 10:
        return "Low Temperature ALert"
    else:
        return "Normal Temperature"
    
print(temperature_alert(42))
print(temperature_alert(8))