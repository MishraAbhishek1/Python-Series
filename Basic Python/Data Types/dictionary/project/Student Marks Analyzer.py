# 💡 LEVEL 3: REAL WORLD MINI PROJECT — Student Marks Analyzer

'''
🎯 Goal:
User se student marks input lena
→ Average calculate karna
→ Highest and lowest student dikhana

'''

students = {}

n  = int(input("enter number of students"))

for i in range(n):
    name = input(f"enter name of student {i+1}:")
    marks = int(input("Enter marks: "))
    students[name] = marks
    
print("\nAll Student Data:", students)

# Average
avg = sum(students.values()) / len(students)
print(f"\nClass Average: {avg}")

# Highest & Lowest
highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print(f"🏆 Topper: {highest} -> {students[highest]}")
print(f"📉 Lowest: {lowest} -> {students[lowest]}")