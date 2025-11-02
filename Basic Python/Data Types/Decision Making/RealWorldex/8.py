# 🔹 7️⃣ Traffic Fine Calculator

def traffic_fine(speed):
    if speed <= 60:
        return "No Fine"
    elif speed <= 100:
        return "Fine: 1000"
    else:
        return "Fine: 25000 (License Seized)"

print(traffic_fine(45))
print(traffic_fine(100))