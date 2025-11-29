# Q9. Function as argument

def apply(fn, x):
    return fn(x)

def square(n):
    return n*n

print(apply(square, 5))