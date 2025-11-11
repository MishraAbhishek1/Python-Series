# here we started logic of paatern and understand the loop and outer loop and inner loop how to work ok brother

# simple in real world projects we use a  for loop  ok ut here we understand when we use a loop like fo r loop and for loop

# simple loop  how to work
for i in range(5):
    print(i)
    
# here we understand structure of two nested loops

# for i in range(rows): # here this loop control outer loop and 
#     for j in range(coulmns): #this loop control inner loop control a column
#         print(...., end = " ")
#     print()

print("----------------------------------------------------------")
# 🧱 STEP 3: Example 1 — Simple Increment Pattern
for i in range(5):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
    
print("----------------------------------------")

# 🧱 STEP 4: Example 2 — Same Number Pattern
for i in range(5):
    for j in range(i+1):
        print(i+1, end=" ")
    print()

print("------------------------------------------------------")
# 🧱 STEP 5: Example 3 — Reverse Pattern
'''
1 2 3 4
1 2 3
1 2
1

'''
for i in range(5):
    for j in range(5-i):
        print(j+1, end=" ")
    print()
        