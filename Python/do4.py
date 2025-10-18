# 4️⃣ Error Handling (Try-Except ka use)

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide(10, 2))    