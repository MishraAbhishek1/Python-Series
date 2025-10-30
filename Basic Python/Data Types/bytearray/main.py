# create a byte array
data = bytearray(b"Python")
print(data)

# here we see a type of byte aray
print(type(data))

# Acess a element
print(data[0])

# Modify element
data[0] = 74
print(data)

# convert to a list
print(list(data))

# Append bytes
data.append(102)
print(data)

# Remove a last item
data.pop()
print(data)

# slice bytearray
print(data[0:3])

# join two bytearays
a = bytearray(b"Hello ")
b = bytearray(b"world")
print(a + b)

# Loop through bytearray
for b in data:
    print(b)
    
# 🔟 Convert back to string
print(data.decode())