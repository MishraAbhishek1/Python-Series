# what is args :

def add_numbers(*args):
    print(args)
    return sum(args)

print(add_numbers(1,2,3,4))

#  2. kwargs kya hota hai?

def user_info(**kwargs):
    print(kwargs)
    
user_info(name="Abhishek", age=22, country="india")

#  3. args + kwargs ek sath

def function(*args, **kwargs):
    print("Args:", args)
    print('kwargs:', kwargs)

function(10,12,30, name="Abhishek", age=22)



# here we make a fucntion 
def my_fucntion():
    print("Hello world")

my_fucntion()

def seno():
    return f"hello Python"
print(seno())