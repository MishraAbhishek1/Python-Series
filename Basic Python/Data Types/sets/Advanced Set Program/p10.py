# 🔟 Exception handling in set operations
s = {1,2,3}
try:
    s.remove(5)
except KeyError:
    print("Element not found safely handled")