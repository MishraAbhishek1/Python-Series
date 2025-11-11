'''
* * * * *
* * * * *
* * * * *
'''

for i in range(3): # outer loop
    for j in range (4): # inner loop
        print("*", end= " ")
    print()

print("--------------------------------------")


# 1️⃣ Square Pattern

for i in range(5):
    for j in range(5):
        print("#", end = '')
    print()

print("--------------------------------------")

# 2️⃣ Right-Angled Triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
    
print("--------------------------------------")

# 3️⃣ Inverted Triangle

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()

print("-------------------------------------------")

# 4️⃣ Number Triangle
for  i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("-------------------------------------------")

# 5️⃣ Reverse Number Triangle

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


print("-----------------------------------------------")

# 🅰️ 1. Alphabet Patterns
ch = 65
for i in range(5):
    for j in range(i+1):
        print(chr(ch), end=' ')
    ch += 1
    print()