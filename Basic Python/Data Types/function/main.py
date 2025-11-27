# ✅ 1. Default Arguments

# when in a function we have a  null value then in a fucniton we use a default value see in program

def welcome_greet(name="Guest"):
    
    return f"Hello world {name}"

print(welcome_greet())
print(welcome_greet("Abhishek"))


# ✅ 2. Keyword Arguments (Named Arguments)

# here we see how we use a keyword arguments ()parameter in arguments we asign a value

def student(name, age):
    print(name, age)
    
student(age=20, name="abhishek")


# ✅ 3. Variable-Length Arguments

# *args multiple positional arguments
def add_all(*numbers):
    return sum(numbers)
print(add_all(1,2,3,4,5))

# ⭐ **kwargs — multiple keyword arguments
def user_info(**data):
    print(data)
user_info(name="abhishek", age=22, city="Delhi")

# 👉 Real use of args + kwargs
# Example: Logging System

def logs(message, **details):
    print(message, details)
logs("Userlogged In", user="Admin", ip="127.0.0.1")


# ✅ 4. Higher-Order Functions

# what is a higher function simply say higher function means we accept a another functtion or return

# where we used : Decorators, middleware, permission systems.

def apply(func, x):
    return func(x)

def square(n):
    return n*n

print(apply(square, 5))

# ✅ 2. Keyword Arguments (Named Arguments)
def student(name, age):
    print(name, age)

student("abhishek", 78)

# Q4. Return multiple values

def calculate(a, b):
    return a+b, a-b, a*b

x, y, z = calculate(10,5)
print(x, y, z)


# *Q5. Variable number of arguments (args)
def total_price(*args):
    return sum(args)
print(total_price(100, 200, 50, 150))

# **Q6. Keyword arguments (kwargs)
# real world user profile update

def user_profile(**kwargs):
    return kwargs

print(user_profile(name="Abhishek", age=22, role="Python Developer"))


# Q7. Function inside function (Nested Function)
def outer():
    def inner():
        return "Inner function"
    return inner()

print(outer())

# Q8. Function returning a function
# (Decorator ka base)

def outer():
    def inner():
        return "I am a inner fucntion"
    return inner

fn = outer()
print(fn())
