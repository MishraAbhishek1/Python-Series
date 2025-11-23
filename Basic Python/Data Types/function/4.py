# 🧠 Example 2: Even & Odd Number Separator

def seperate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

print(seperate_even_odd([1,2,3,4,5,5,6,7,8,9,10]))