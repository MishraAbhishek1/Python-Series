# 3️⃣ Safe access using get()

student = {"name": "Abhishek", "age": 22, "course": "AI"}
print(student.get("rool_no", "Key not found"))

# 4️⃣ Add new key-value pair
student["city"] = "Delhi"
print(student)

# 5️⃣ Update existing key
student["age"] = 25
print(student)

# 6️⃣ Remove a key using pop()
student.pop("course")
print(student)

# 7️⃣ Remove last item
student.popitem()
print(student)

# 8️⃣ Get all keys
print(student.keys())

# 9️⃣ Get all values
print(student.values())

# 🔟 Clear dictionary
student.clear()
print(student)