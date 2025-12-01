# 5) Mutable default-argument PITFALL (must-know)

def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))

# here i don't know why it s output ists very different first print is [1], second output is [1,2]

# here we fix the problem

def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))

# 6) Scope: local, global, nonlocal — rules + examples

x = 10 # global variable

def fn():
    x = 5 # local varaible
    return x

print(fn())
print(x)

# Changing global variable (use global)

count = 0

def inc():
    global count
    count += 1
    
inc()
print(count)