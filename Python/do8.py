# 8️⃣ Data Validation (like form fields)

def validate_user_data(data):
    required_fields = ["username", "email", "age"]
    
    for field in required_fields:
        if field not in data:
            return f"Error: Missing field '{field}"
    return "All required fields are present"

print(validate_user_data({"username": "user1", "email": "abhi@com", "age": 25}))
print(validate_user_data({"na"}))    