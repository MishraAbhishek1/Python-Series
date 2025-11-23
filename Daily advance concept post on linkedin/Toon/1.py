import json

# Step 1: Create Student JSON (Python dict)
student_json = {
    "name": "Abhishek Kumar",
    "roll": 2121932,
    "branch": "CSE",
    "year": 4,
    "skills": ["Python", "Django", "FastAPI"]
}

#  Convert JSON → TOON
def json_to_toon(data):
    toon_list = []
    for key, value in data.items():
        toon_list.append([key, value])
    return toon_list

# Convert
toon_output = json_to_toon(student_json)

# Step 3: Print Output in Terminal
print("Original JSON:")
print(json.dumps(student_json, indent=2))

print("\nConverted TOON:")
print(toon_output)
