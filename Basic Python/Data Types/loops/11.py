# 1. ATM Pin Try

pin = "1234"
tries = 0
while tries < 3:
    entered = input("Enter PIN: ")
    if entered == pin:
        print("Acces Granted ")
        break
    else:
        print("Wrong PIN")
        tries += 1
        