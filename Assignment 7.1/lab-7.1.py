#Task 1
#Buggy Code:
'''def greet():
print "Hello, AI Debugging Lab!"
greet()'''
#Fixed Code:
def greet():
    print("Hello, AI Debugging Lab!")
greet()
#Explanation: The original code is missing parentheses around the print statement, which is required in Python 3. In the fixed code, we add parentheses around the string in the print function, allowing the code to execute correctly and print the greeting message. 

#Task 2
#Buggy Code:
'''def check_number(n):
if n = 10:
return "Ten"
else:
return "Not Ten"'''
#Fixed Code:
def check_number(n):
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"
print(check_number(10)) 
#Explanation: The original code uses a single equals sign (=) for comparison, which is incorrect and raises a SyntaxError. In the fixed code, we use a double equals sign (==) to compare the value of n with 10, allowing the function to return "Ten" when n is 10 and "Not Ten" otherwise.

#Task 3
#Buggy Code:
'''def read_file(filename):
with open(filename, 'r') as f:
return f.read()
print(read_file("nonexistent.txt"))'''
#Fixed Code:
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."
print(read_file("nonexistent.txt"))
#Explanation: The original code attempts to read a file that does not exist, which raises a FileNotFoundError. In the fixed code, we wrap the file reading operation in a try-except block to catch the FileNotFoundError and return a user-friendly message instead of crashing the program.

#Task 4
#Buggy Code:
'''class Car:
def start(self):
return "Car started"
my_car = Car()
print(my_car.drive()) # drive() is not defined'''
#Fixed Code:
class Car:
    def start(self):
        return "Car started"
    def drive(self):
        return "Car is driving"
my_car = Car()
print(my_car.drive())
#Explanation: The original code tries to call a method drive() that is not defined in the Car class, which raises an AttributeError. In the fixed code, we define the drive() method within the Car class, allowing us to call it without any errors and return a message indicating that the car is driving.   

#Task 5
#Buggy Code:
'''def add_five(value):
return value + 5
print(add_five("10"))'''
#Fixed Code:
def add_five(value):
    try:
        return int(value) + 5
    except ValueError:
        return "Invalid input: Please enter a number."
print(add_five("10"))
#Explanation: The original code attempts to add 5 to a string "10", which raises a TypeError. In the fixed code, we convert the input value to an integer using int() before performing the addition. We also include a try-except block to catch any ValueError that may occur if the input cannot be converted to an integer, providing a user-friendly error message instead.
