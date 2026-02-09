#Task 1
#Buggy Code:
'''def add_item(item, items=[]):
   items.append(item)
   return items
print(add_item(1))
print(add_item(2))'''
#Fixed Code:
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1))
print(add_item(2))
#Explanation: The original code uses a mutable default argument (a list) which is shared across all calls to the function. This means that when you append an item to the list in one call, it affects all subsequent calls that use the default list. In the fixed code, we use None as the default value and create a new list inside the function if items is None. This ensures that each call to add_item gets its own separate list.

#Task 2
#Buggy Code:
'''def check_sum():
   return (0.1 + 0.2) == 0.3
print(check_sum())'''
#Fixed Code:
def check_sum():
    return abs((0.1 + 0.2) - 0.3) < 1e-9
print(check_sum())
#Explanation: The original code checks if the sum of 0.1 and 0.2 is exactly equal to 0.3, which can lead to a false result due to floating-point precision issues. In the fixed code, we check if the absolute difference between (0.1 + 0.2) and 0.3 is smaller than a very small number (1e-9), which accounts for the precision error and gives a more accurate result.

#Task 3
#Buggy Code:
'''def countdown(n):
   print(n)
   return countdown(n-1)
countdown(5)'''
#Fixed Code:
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n-1)
countdown(5)
#Explanation: The original code does not have a base case to stop the recursion, which leads to a maximum recursion depth error when n becomes negative. In the fixed code, we add a base case that checks if n is less than 0, at which point the function returns and stops the recursion. This allows the countdown to work correctly without causing an error.

#Task 4
#Buggy Code:
'''def get_value():
   data = {"a": 1, "b": 2}
   return data["c"]
print(get_value())'''
#Fixed Code:
def get_value():
    data = {"a": 1, "b": 2}
    return data.get("c", "Key not found")
print(get_value())
#Explanation: The original code tries to access a key "c" that does not exist in the dictionary, which raises a KeyError. In the fixed code, we use the get method of the dictionary, which allows us to specify a default value ("Key not found") to return if the key is not found. This prevents the error and provides a more user-friendly message.

#Task 5
#Buggy Code:
'''def loop_example():
   i = 0
   while i < 5:
       print(i)'''
#Fixed Code:
def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1
loop_example()
#Explanation: The original code has an infinite loop because the variable i is never incremented, which means it will always be less than 5. In the fixed code, we add i += 1 inside the loop to ensure that i is incremented on each iteration, allowing the loop to eventually terminate when i reaches 5.

#Task 6
#Buggy Code:
'''a, b = (1, 2, 3)'''
#Fixed Code:
# Bug: Wrong unpacking
a, b, *rest = (1, 2, 3)
print(a)  # Output: 1
print(b)  # Output: 2
print(rest)  # Output: [3]
# Explanation: The original code tries to unpack a tuple with three values into two variables, which raises a ValueError. In the fixed code, we use the *rest syntax to capture any extra values in a list called rest. This allows us to unpack the first two values into a and b while still keeping the remaining value in rest without causing an error.

#Task 7
#Buggy Code:
'''def func():
   x = 5
       y = 10
   return x+y'''
#Fixed Code:
def func():
    x = 5
    y = 10
    return x + y
print(func())
#Explanation: The original code has inconsistent indentation, which leads to an IndentationError. In the fixed code, we ensure that all lines of code within the function have the same level of indentation. This allows the function to execute properly and return the correct result when called.

#Task 8
#Buggy Code:
'''import maths
print(maths.sqrt(16))'''
#Fixed Code:
# Bug: Wrong import
import math
print(math.sqrt(16))
# Explanation: The original code tries to import a module named "maths", which does not exist in the Python standard library. The correct module name is "math". In the fixed code, we change the import statement to import math, which allows us to use the sqrt function correctly and get the expected output of 4.0 when calculating the square root of 16.    

#Task 9
#Buggy Code:
'''def total(numbers):
   for n in numbers:
       return n
print(total([1,2,3]))'''
#Fixed Code:
def total(numbers):
    total_sum = 0
    for n in numbers:
        total_sum += n
    return total_sum
print(total([1, 2, 3]))
#Explanation: The original code returns the first number in the list because the return statement is inside the loop, which causes the function to exit after the first iteration. In the fixed code, we initialize a variable total_sum to 0 and add each number in the list to total_sum within the loop, ensuring that all numbers are summed correctly before returning the total.

#Task 10
#Buggy Code:
'''def calculate_area():
   return length * width
print(calculate_area())'''
#Fixed Code:
def calculate_area(length, width):
    return length * width
print(calculate_area(5, 3))
#Explanation: The original code tries to calculate the area using variables length and width that are not defined within the function, which raises a NameError. In the fixed code, we modify the function to accept length and width as parameters, allowing us to pass the necessary values when calling the function. This way, we can calculate the area correctly and get the expected output of 15 when calculating the area of a rectangle with length 5 and width 3.    

#Task 11
#Buggy Code:
'''def add_values():
   return 5 + "10"
print(add_values())'''
#Fixed Code:
def add_values():
    return 5 + int("10")
print(add_values())
#Explanation: The original code tries to add an integer (5) and a string ("10"), which raises a TypeError. In the fixed code, we convert the string "10" to an integer using the int() function before performing the addition. This allows us to successfully add the two values and get the expected output of 15.

#Task 12
#Buggy Code:
'''def combine():
   return "Numbers: " + [1, 2, 3]
print(combine())'''
#Fixed Code:
def combine():
    return "Numbers: " + str([1, 2, 3])
print(combine())
#Explanation: The original code tries to concatenate a string with a list, which raises a TypeError. In the fixed code, we convert the list [1, 2, 3] to a string using the str() function before concatenating it with the "Numbers: " string. This allows us to successfully combine the string and the list representation, resulting in the output "Numbers: [1, 2, 3]".    

#Task 13
#Buggy Code:
'''def repeat_text():
   return "Hello" * 2.5
print(repeat_text())'''
#Fixed Code:
def repeat_text():
    return "Hello" * 2
print(repeat_text())
#Explanation: The original code tries to multiply a string by a non-integer (2.5), which raises a TypeError. In the fixed code, we change the multiplier to an integer (2), which allows us to repeat the string "Hello" twice successfully, resulting in the output "HelloHello".  

#Task 14
#Buggy Code:
'''def compute():
   value = None
   return value + 10
print(compute())'''
#Fixed Code:
def compute():
    value = 0
    return value + 10
print(compute())
#Explanation: The original code initializes the variable value to None, which cannot be added to an integer, resulting in a TypeError. In the fixed code, we initialize value to 0, which allows us to perform the addition without any errors. The function now returns 10, which is the expected output when adding 10 to the initial value of 0. 

#Task 15
#Buggy Code:
'''def sum_two_numbers():
   a = input("Enter first number: ")
   b = input("Enter second number: ")
   return a + b
print(sum_two_numbers())'''
#Fixed Code:
def sum_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a + b
print(sum_two_numbers())
#Explanation: The original code takes user input as strings, and when it tries to add them together, it concatenates the strings instead of performing numerical addition, which is not the intended behavior. In the fixed code, we convert the input strings to floats using the float() function before performing the addition. This allows us to correctly sum the two numbers and return the expected numerical result.   
