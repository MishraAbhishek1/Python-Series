# 🧠 Example 5: Student Marks Evaluation

def evaluate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    else:
        grade = 'C'
    return total, average, grade

results = evaluate_marks([85, 92, 78, 90, 88])
print(results)