# 🔹 10. Tuple Immutability
nums = (1, 2, 3, 4, 5)
print("original tuple:", nums)
try:
    nums[0] = 10
except TypeError as e:
    print("Error:", e)