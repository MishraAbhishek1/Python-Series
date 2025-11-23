# 🧠 Example 1: Sum of 1 to n
def sumOfn(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sumOfn(10))