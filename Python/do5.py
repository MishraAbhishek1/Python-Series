# 5️⃣ User Input Sanitization

def sanitize_input(data):
    return data.strip().replace("<", "&lt;").replace(">", "&gt;")

print(sanitize_input("  <script>alert(1)</script>  "))
