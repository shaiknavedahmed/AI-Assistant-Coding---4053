#Task 1
'''Generate a Python class named Student with attributes name, roll number, and branch.
Include a constructor (__init__) to initialize these attributes and a method display_details() to print the student information.
Create a sample Student object, execute the code, and display the output.
Finally, provide a brief analysis of the code focusing on correctness and clarity.'''
class Student:
    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")
# Creating a sample Student object
student1 = Student("Alice", "101", "Computer Science")
# Displaying the student details
student1.display_details()  
student2 = Student("Bob", "102", "Mechanical Engineering")
student2.display_details()
student3 = Student("Charlie", "103", "Electrical Engineering")
student3.display_details()


#Task 2
'''Generate a Python function that prints the first 10 multiples of a given number using a for loop.
Analyze and explain the loop logic briefly.
Then generate another version of the same function using a while loop instead of a for loop.
Display sample output and compare both looping approaches in terms of clarity and control.'''
def print_multiples_for_loop(number):
    print(f"First 10 multiples of {number} using for loop:")
    for i in range(1, 11):
        print(number * i)
# Sample output using for loop
print_multiples_for_loop(5)
def print_multiples_while_loop(number):
    print(f"First 10 multiples of {number} using while loop:")
    i = 1
    while i <= 10:
        print(number * i)
        i += 1
# Sample output using while loop
print_multiples_while_loop(5)

#Task 3
'''Generate a Python function that classifies a person into age groups (Child, Teenager, Adult, Senior) using nested if–elif–else statements.
Analyze and explain the conditional logic used.
Then generate an alternative implementation using simplified conditions or a dictionary-based approach, and explain how it differs from the first method.'''
def classify_age_group(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 60:
        return "Adult"
    else:
        return "Senior"
# Sample output using nested if-elif-else
ages = [10, 15, 25, 65]
for age in ages:
    print(f"Age {age} is classified as: {classify_age_group(age)}")
def classify_age_group_dict(age):
    age_groups = {
        range(0, 13): "Child",
        range(13, 20): "Teenager",
        range(20, 60): "Adult",
        range(60, 150): "Senior"
    }
    for age_range, group in age_groups.items():
        if age in age_range:
            return group
# Sample output using dictionary-based approach
for age in ages:
    print(f"Age {age} is classified as: {classify_age_group_dict(age)}")

#Task 4
'''Generate a Python function sum_to_n(n) that calculates the sum of the first n natural numbers using a for loop.
Analyze and briefly explain how the loop works.
Then suggest an alternative implementation using either a while loop or a mathematical formula, and compare the approaches in terms of simplicity and efficiency.'''
def sum_to_n_for_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
# Sample output using for loop
n = 10
print(f"Sum of first {n} natural numbers using for loop: {sum_to_n_for_loop(n)}")
def sum_to_n_formula(n):
    return n * (n + 1) // 2
# Sample output using mathematical formula
print(f"Sum of first {n} natural numbers using formula: {sum_to_n_formula(n)}")

#Task 5
'''Generate a Python function sum_to_n(n) that calculates the sum of the first n natural numbers using a for loop.
Analyze and briefly explain how the loop works.
Then suggest an alternative implementation using either a while loop or a mathematical formula, and compare the approaches in terms of simplicity and efficiency.'''
def sum_to_n_for_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
# Sample output using for loop
n = 10
print(f"Sum of first {n} natural numbers using for loop: {sum_to_n_for_loop(n)}")
def sum_to_n_formula(n):
    return n * (n + 1) // 2
# Sample output using mathematical formula
print(f"Sum of first {n} natural numbers using formula: {sum_to_n_formula(n)}")
