# 🔹 9️⃣ Movie Ticket Booking System

def ticket_price(age):
    if age <= 5:
        return "Free Entry"
    elif age <= 18:
        return "Ticket Price: 100"
    elif age <= 60:
        return "Ticket Price: 200"
    else:
        return "senior Discount: 150"

print(ticket_price(5))