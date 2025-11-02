# 4️⃣ Default parameter as None

def multiply(a, b=None):
    if b is None:
        b = 1
    return a*b

print(multiply(5))

# 4️⃣ Default parameter as None

value = None
if not value:
    value = "Intialized"

print(value)