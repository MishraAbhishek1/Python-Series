data = bytearray(b"Abhi")
mv = memoryview(data)
print(mv)

# create memoryview
data = bytearray(b"Abhishek")

# acess data via slice
print(mv[0:4].tobytes())

# modify using memoryoverview
mv[0] = 74
print(data)

# Length of memoryview
print(len(mv))

# ierate memryview
for i in mv:
    print(i)
    
# Convert memoryview to list
print(list(mv))

# 🔟 Release memoryview
mv.release()
print("Released memory view")
