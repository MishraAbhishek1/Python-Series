#  User Authentication Logic (Manual way)

users = {"admin": "admin123", "alpha": "abc123"}

def authenticate(username, password):
    if username in users and users[username] == password:
        return "Login successful"
    else:
        return "Invalid credentials"

print(authenticate("admin", "admin123"))    