# 5️⃣ Remove element using remove()
# (throws error if not found)

s = {1, 2, 3 ,4}
try:
    s.remove(5)
except KeyError:
    print("Element not found")

print(s)