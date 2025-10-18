# 7️⃣ JSON Data Parsin

import json

def parse_json(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return "Error: Invalid json data"
    
print(parse_json('{"name": "Alice", "age": 30}'))    