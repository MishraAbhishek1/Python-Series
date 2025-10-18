# 16️⃣ File Upload Validation

def validate_file(filename):
    allowed = ["jpg", "png", 'gif']
    if any(filename.endswith(ext) for ext in allowed):
        return "File Accepted"
    return "Invalid File Type"
print(validate_file("image.jpg"))
print(validate_file("document.pdf"))