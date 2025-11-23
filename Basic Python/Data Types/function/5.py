# 🧠 Example 4: Password Checker (Login Simulation)

def login_system():
    correct_password = "admin@123"
    attempt = 0
    
    while True:
        password = input("Enter the password: ")
        attempt += 1
        if password == correct_password:
            print("Successfully logged in!")
            break
        elif attempt == 3:
            print("Too many failed attempts. Try later")
            break
        else:
            print("wrong Password, Try again")
    
login_system()