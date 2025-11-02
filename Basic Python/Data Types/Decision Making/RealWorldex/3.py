# 🔹 1️⃣ Age Eligibility Checker

def check_age(age):
    if age < 0:
        return "Invalid Age"
    elif age < 18:
        return "Minor - Not eligible for voting"
    else:
        return "Adult - Eligible for votting"

print(check_age(17))