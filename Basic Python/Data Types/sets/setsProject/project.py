# 💡 LEVEL 3: REAL-WORLD MINI PROJECT — Duplicate Email Finder
emails = [
    "test@gmail.com",
    "info@yahoo.com",
    "test@gmail.com",
    "hello@gmail.com",
    "info@yahoo.com"
]

try:
    # here we find a duplicate emails >
    total = len(emails)
    unique_emails = set(emails)
    duplicates = total - len(unique_emails)
    
    print("unique emails: ", unique_emails)
    print("total emails: ", total)
    print("duplicate count: ", duplicates)
    
    if duplicates > 0:
        print("Sugestion: clean your contact list:")
    
    else:
        print("All emails are unique")
        
except Exception as e:
    print("Error occured:", e)        