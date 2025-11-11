# print 1 to 10
i = 1
while i <=10:
    print(f"print  number: {i}")
    i += 1


# Real Life Example
goals = 0
while goals < 10:
   print("Practicing... ⚽")
   goals += 1
    
# 🧮 6️⃣ Example 2 — User Input Until Correct

correct_password = "admin@123"

while True:
    user_input = input("Enter the password:")
    # set a limit to number of attempts
    
    if user_input == correct_password:
        print("Succesfuuly login")
        break
    else:
        print("incorrect password, try again")