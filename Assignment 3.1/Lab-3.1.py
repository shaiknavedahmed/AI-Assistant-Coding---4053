'''#Write a Python function that checks whether a given integer is a palindrome.The function should return True if the number is a palindrome and False otherwise Do not convert the number to a string.
def is_palindrome(num):
    if num < 0:
        return False
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original_num == reversed_num
# Example usage:
print(is_palindrome(121))  # True
print(is_palindrome(-121)) # False
print(is_palindrome(10))   # False
print(is_palindrome(12321))# True

#Now write a Python function that takes an integer as input and returns the factorial of that number.Handle invalid inputs such as negative numbers appropriately.
def factorial(n):
    if n < 0:
        return "Invalid input: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Example usage:
print(factorial(5))  # 120
print(factorial(0))  # 1
print(factorial(-3)) # Invalid input: Factorial is not defined for negative numbers.
print(factorial(7))  # 5040

#Now write a Python function that takes an integer as input and checks whether it is an Armstrong number. The function should print "Armstrong Number" if it is, otherwise "Not an Armstrong Number".
def is_armstrong_number(num):
    if num < 0:
        print("Not an Armstrong Number")
        return
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_powers == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
# Example usage:
is_armstrong_number(153)  # Armstrong Number
is_armstrong_number(123)  # Not an Armstrong Number
is_armstrong_number(9474) # Armstrong Number 
is_armstrong_number(-5)   # Not an Armstrong Number
is_armstrong_number(370)  # Armstrong Number

#Generate an optimized Python program to classify an integer as Prime, Composite, or Neither.Constraints: validate input, check divisibility up to √n, print only one result (Prime, Composite, or Neither), and briefly compare with a basic approach.
import math
def classify_integer(n):
    if not isinstance(n, int):
        return "Invalid input: Please enter an integer."
    if n < 2:
        return "Neither"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Composite"
    return "Prime"
# Example usage:
print(classify_integer(11))  # Prime
print(classify_integer(15))  # Composite
print(classify_integer(1))   # Neither
print(classify_integer(-5))  # Neither
print(classify_integer(2))   # Prime

#Write a Python function that checks whether a given integer is a Perfect Number.Constraints: handle 0, 1, and negative numbers, use an efficient divisor check, and print Perfect Number or Not a Perfect Number.
def is_perfect_number(n):
    if n <= 1:
        print("Not a Perfect Number")
        return
    sum_of_divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != 1 and i != n // i:
                sum_of_divisors += n // i
    if sum_of_divisors == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
# Example usage:
is_perfect_number(6)    # Perfect Number
is_perfect_number(28)   # Perfect Number      
is_perfect_number(12)   # Not a Perfect Number
is_perfect_number(1)    # Not a Perfect Number
'''
#Write a Python program to check if a number is Even or Odd with input validation.Examples: Input: 8 → Output: Even Input: 15 → Output: Odd Input: 0 → Output: Even Constraints: Handle non-integer inputs and negative numbers. Print only Even or Odd.
def check_even_odd(value=None):
    try:
        if value is None:
            value = input()
        num = int(value)
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except (ValueError, TypeError):
        pass  # print nothing for invalid input

# Example usage:
check_even_odd(15)   # Odd
check_even_odd(8)    # Even
check_even_odd(0)    # Even
check_even_odd(-3)   # Odd
