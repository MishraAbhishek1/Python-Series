# 6️⃣ Count frequency of words

text = "python python django flask django"
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)