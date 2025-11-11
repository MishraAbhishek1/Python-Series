ch = 65
for i in range(5):
  for j in range(i+1):
      print(chr(ch), end=" ")
      ch += 1
  print()
  

print("*************************************************")

i = 0
for i in range(5):
    for j in range(i+1):
        print(i, end = " ")
        i += 1
    print()
    
print("**************************************************")

for i in range(5):
    for j in range(i+1):
        print(j+1, end = " ")
    print()

print("----------------------------------------------")
num = 1
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()