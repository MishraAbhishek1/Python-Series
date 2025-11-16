# # print 1 to 10
# i = 1
# while i <=10:
#     print(f"print  number: {i}")
#     i += 1


# # Real Life Example
# goals = 0
# while goals < 10:
#    print("Practicing... ⚽")
#    goals += 1
    
# # 🧮 6️⃣ Example 2 — User Input Until Correct

# correct_password = "admin@123"

# while True:
#     user_input = input("Enter the password:")
#     # set a limit to number of attempts
    
#     if user_input == correct_password:
#         print("Succesfuuly login")
#         break
#     else:
#         print("incorrect password, try again")

# # 6️⃣ Print multiplication table of a number
# n = int(input("Enter a number to print its multiple: "))
# i = 1
# while i <= 10:
#     print(f"{n}*{i} = {n*i}")
#     i += 1
    
# # 7️⃣ Count digits in a number
# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print("Total digits:", count)

# 8️⃣ Sum of digits of a number

n = int(input("Enter a number:"))
sum = 0
while n > 0:
    # print(n)
   sum += n %10
   n //= 10
print("Sum of digits:", sum)