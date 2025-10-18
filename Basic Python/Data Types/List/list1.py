# 🧩 4. List ke Basic Operations

# create a list of fruits
numbers = [1,2,3,4,5]

print("Original List:", numbers)

# aceessing first element
print("First Element:", numbers[0])

# Modify a list at index 2
numbers[2] = 10
print("Modified List:", numbers)

# Append a new element to the list
numbers.append(6)
print("List after Append:", numbers)

# Remove an element from the list
numbers.remove(4)
print("List after Remove:", numbers)

# Length of the list
print("Length of list: ", len(numbers))

# Slicing the list
print("Sliced list (index 1 to 3):", numbers[1:4])

# Iterate through the list
for num in numbers:
    print("Numbers: ", num)