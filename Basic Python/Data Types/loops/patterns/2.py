# 2️⃣ Continuous Alphabet Sequence

ch = 65
for i in range(5):
    for j in range(i+1):
        print(chr(ch), end=" ")
    ch += 1
    print()
    
print("-----------------------------------------")

ch = 65
for i in range(5):
    for j in range(i+1):
        print(chr(ch), end= " ")
        ch += 1
    print()

print("----------------------------------------------")

for i in range(1,6):
    print(" " * (5 - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()