# 2. Login Retry

correct_user = "admin"
while True:
    user = input("Enter username: ")
    if user == correct_user:
        print("Welcome Admin")
        break
        # continue
    else:
        print("Try Again...")