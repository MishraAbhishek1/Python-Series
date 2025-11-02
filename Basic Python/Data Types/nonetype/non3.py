# Default value ke liye

def show_message(msg=None):
    if msg is None:
        msg = "Default Message"
    print(msg)

show_message()
show_message("Hi!")