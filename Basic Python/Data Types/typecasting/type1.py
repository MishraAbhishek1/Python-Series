# # 🟢 1️⃣ Implicit Type Casting (Automatic Conversion)
# # Python automatically type convert karta hai jab data loss nahi hota.

# a = 5
# b = 2.5

# result = a+b
# print(result)
# print(type(result))

# # 🔸 String → Integer / Float
# print("----------------------------------------------")
# a = "10"
# print(int(a))
# print(float(a))


# 🔸 Integer / Float → String
print("-------------------------------------------------------")

a = 42
b = 3.14

print(str(a))
print(str(b))

# print(str(type(a)))

# 🔸 List ↔ Tuple
print('------------------------------------------------')

my_list = [1,2,3,4]
my_tuple = tuple(my_list)

print(my_tuple)

# 🔸 List / Tuple → Set
print("------------------------------------------------------")

nums = [1,2,3,3,4,5,6]

unique = set(nums)
print(unique)

# 🔸 Set → List

print("--------------------------------------------------------")

s = {10, 20, 30}
print(list(s))

# 🔸 Bytes ↔ Bytearray
print('-----------------------------------------------------------------')

b = bytes("abhi", "utf-8")
print(b)

ba = bytearray(b)
print(b)

# 🔸 List of tuples → Dictionary
print('-------------------------------------------------------')

pairs = [("name", "Abhishek"), ("age", 22)]
print(dict(pairs))

# 🔸 Int / Float → Complex
print('---------------------------------------------------')
x = 5
y = 3

print(complex(x,y))