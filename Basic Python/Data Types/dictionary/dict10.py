# 7️⃣ Remove all items having specific value

data = {"a": 1, "b": 2, "c": 1, "d": 3}
clean = {k: v for k, v in data.items() if k != "a"}
print(clean)

# 8️⃣ Sort dictionary by value
marks = {"abhi": 89, "Rohit": 95, "Neha": 78}
sorted_dict = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)

# 9️⃣ Handle missing key safely (try–except)
student = {"name": "Abhi"}
try:
    print(student["age"])
except KeyError:
    print("Key not Found")
    
# 🔟 Combine two lists into dict
keys = ["name", "age", "city"]
values = ["Abhi", 22, "Delhi"]
d = dict(zip(keys, values))
print(d)