# 3) Forwarding arguments (unpacking)

# when we forward any value one funciton to another fucntion

def foo(a, b, c=3):
    return a+b+c

nums = (1,2)
# kw = {'c':0}

# print(foo(*nums, **kw))
print(foo(*nums))

# see here we positional- only / keyword-only (advances but pratical)

def f(a, b, /, c, *, d=4):
    return a+b+c+d

print(f(1,2,3, d=5))


print(type(None))

# 🔥 3. Why we use None? (Real Use Cases)

# because we need a default arguments

# def connect(host=None):
#     if host is None:
#         # host = "localhost"
#         # host = " "
#     print("Connecting to:", host)

# connect()

# def connect(host=None):
#     host = input("Enter the host name:")
#     if host is None:
#         return f"host is not avaliable"
#     print(host)

# connect()

# this is not a corrent logic because we nee  check none is true because when we enter a  empty srting count " ",
# tha t reaso  coorect logic is here,

def connecthost(host = None):
    host = input("Enter the host name: ")
    
    if host.strip() == "":
        return "host is not available"
    
    print("hosts:", host)

connecthost()