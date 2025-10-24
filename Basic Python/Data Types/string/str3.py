# 3️⃣ Count vowels

s= "Machine Learning"
count = 0
for i in s:
    if i.lower() in "aeiou":
        count += 1

print("Total Vowels:", count)