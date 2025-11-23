# here we make a function that checks if the first character of any string in the list is 'x'
def my_function(m):
    m = ['x', 'y', 'z']
    for item in m:
        if item[0] == 'x':
            return True
        else:
            return False
print(my_function([0]))

# in this function we define a function that 