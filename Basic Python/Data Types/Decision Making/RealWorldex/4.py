# 🔹 2️⃣ Login Authentication System

def authenticate(username, password):
    if username == "admin" and password == "1234":
        return "login Successful"
    
    else:
        return "invalid credentails"
    
print(authenticate("admin", "1234"))
print(authenticate("user", "576"))