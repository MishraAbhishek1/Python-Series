import json

file_path = "data.json"

# Here we read a JSON file
def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file) 
        return data

# Main Program
json_data = read_json_file(file_path)

print("JSON Data Successfully Read:")
print(json_data)
