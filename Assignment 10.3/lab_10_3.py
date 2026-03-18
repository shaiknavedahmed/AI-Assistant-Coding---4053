#Task1
def factorial(n):
    result = 1
    for i in range(1, n):
        result = result * i
    return result

print(factorial(5))
#Corrected Code
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print(factorial(5))
#Explanation: The original code for the factorial function had a logical error in the loop. The loop was iterating from 1 to n-1, which means it was not including n in the multiplication. To fix this, we need to change the loop to iterate from 1 to n (inclusive). This can be achieved by changing the range to `range(1, n + 1)`.  

#Task2
'''def calc(a, b, c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":'''
#Corrected Code
def calc(a, b, c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Supported operations are: add, sub, mul, div.")
print(calc(5, 3, "add"))   # 8
print(calc(10, 2, "div"))  # 5.0
#Explanation: The original code for the calc function did not handle the case where the operation is "div" and the second operand (b) is zero, which would result in a division by zero error. To fix this, we need to add a check for b being zero before performing the division. If b is zero, we raise a ValueError with an appropriate message. Additionally, we should also handle the case where an invalid operation is passed to the function by adding an else clause that raises a ValueError for unsupported operations.

#Task3
def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(Checkprime(5))   # True
print(Checkprime(4))   # False
#PEP8 Style Guide with complete code
def check_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check for primality.
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(check_prime(5))   # True
print(check_prime(4))   # False
#Explanation: The original code for the Checkprime function did not handle the case where n is less than or equal to 1, which are not prime numbers. To fix this, we need to add a check at the beginning of the function to return False if n is less than or equal to 1. Additionally, we can optimize the loop by only iterating up to the square root of n, since if n is divisible by any number greater than its square root, it must have already been divisible by a smaller number. This can be achieved by changing the loop to `for i in range(2, int(n**0.5) + 1)`. Finally, we should also follow PEP8 style guidelines by using lowercase letters and underscores for function names, so we rename the function to `check_prime`.

#Task 4
'''def processData(d):
    return [x * 2 for x in d if x % 2 == 0]
print(multiply_even_numbers([1, 2, 3, 4]))          # [4, 8]
print(multiply_even_numbers([2, 6, 7], 3))          # [6, 18]
print(multiply_even_numbers([]))                    # []'''
#PEP8 Style Guide with complete code
def multiply_even_numbers(d):
    """
    Multiply even numbers in a list by 2.

    Args:
        d (list): A list of integers.
    Returns:
        list: A list containing the even numbers from the input list multiplied by 2.
    """
    return [x * 2 for x in d if x % 2 == 0]
print(multiply_even_numbers([1, 2, 3, 4]))          # [4, 8]
print(multiply_even_numbers([2, 6, 7]))          # [4, 12]
print(multiply_even_numbers([]))                    # []
#Explanation: The original code for the processData function was not following PEP8 style guidelines, and the function name was not descriptive of its purpose. To fix this, we rename the function to `multiply_even_numbers` to better reflect its functionality. Additionally, we should remove the second argument from the example usage, as the function only takes one argument (the list of numbers). Finally, we should also add a docstring to the function to explain its purpose, parameters, and return value. 

#Task5
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
numbers = range(1000000)
#Optimized High-Performance Code with numpy
import numpy as np
def sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers.

    Args:
        numbers (iterable): An iterable of numerical values.
    Returns:
        float: The sum of squares of the input numbers.
    """
    return np.sum(np.square(numbers))
numbers = np.arange(1000000)
#Execution time comparision code
import time
# Original code execution time
start_time = time.time()
numbers = range(1000000)
print(sum_of_squares(numbers))
end_time = time.time()
print(f"Original code execution time: {end_time - start_time} seconds")
# Optimized code execution time
start_time = time.time()
numbers = np.arange(1000000)
print(sum_of_squares(numbers))
end_time = time.time()
print(f"Optimized code execution time: {end_time - start_time} seconds")
#Explanation: The original code for the sum_of_squares function uses a for loop to iterate through the list of numbers and calculate the sum of squares, which can be inefficient for large lists. To optimize this, we can use the NumPy library, which provides efficient functions for array operations. We can use `np.square` to calculate the squares of the numbers and `np.sum` to calculate the total sum of those squares. This approach is much faster, especially for large lists, as it takes advantage of NumPy's optimized C and Fortran code under the hood. Additionally, we should also add a docstring to the function to explain its purpose, parameters, and return value.


