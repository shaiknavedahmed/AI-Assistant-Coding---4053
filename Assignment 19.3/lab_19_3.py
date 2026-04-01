'''Task 1 – Python to C++ Conversion
Task:
Translate a simple Python class into C++ using AI assistance.
Instructions:
• Prompt AI to convert a Python class representing a Student
with attributes and methods into equivalent C++ code
• Ensure proper handling of:
o Constructors
o Data types
o Access specifiers
• Compile and run both versions to verify output consistency
Expected Output:
An equivalent working C++ class translated from Python.'''
'''# Python code for the Student class
from ast import main


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Example usage
student1 = Student("Alice", 20)
student1.display_info()
// C++ code for the Student class
#include <iostream>
#include <string>   
class Student {
private:
    std::string name;
    int age;
public:
    Student(std::string name, int age) {
        this->name = name;
        this->age = age;
    }
    void display_info() {
        std::cout << "Name: " << name << ", Age: " << age << std::endl;
    }
}; 
int main() {
    Student student1("Alice", 20);
    student1.display_info();
    return 0;
}
'''

'''Task 2 – Java to Python Function Conversion
Task:
Convert a Java method that checks whether a number is prime into
Python.
Instructions:
• Ask AI to translate a Java isPrime() method into Python
• Test the function with multiple inputs
• Ensure the Python version follows Pythonic syntax and logic
Expected Output:
A correct Python function equivalent to the original Java prime-
checking method.'''
'''// Java code for the isPrime method
public static boolean isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}'''
'''# Python code for the isPrime function
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# Testing the is_prime function
test_numbers = [1, 2, 3, 4, 5, 10, 11, 13, 15, 17]
for num in test_numbers:
    print(f"{num} is prime: {is_prime(num)}")  ''' 

'''Task 3 – Pseudocode to Python Implementation
Task:
Translate a given pseudocode algorithm into Python using AI.
Instructions:
• Provide AI with pseudocode for sorting numbers (e.g.,
bubble sort or selection sort)
• Ask AI to convert it into executable Python code
• Validate correctness using sample input lists
Expected Output:
A working Python program that correctly implements the
pseudocode logic.'''
'''Pseudocode for Bubble Sort:
function bubbleSort(arr):
    n = length of arr
    for i from 0 to n-1:
        for j from 0 to n-i-2:
            if arr[j] > arr[j+1]:
                swap arr[j] and arr[j+1]
    return arr
'''
'''# Python code for Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Testing the bubble_sort function
test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(test_list)
print("Sorted array is:", sorted_list)'''

'''Task:
Translate a SQL query into a Pandas DataFrame operation in
Python.
Instructions:
• Provide AI with a SQL query (e.g., SELECT name, salary
FROM employees WHERE salary > 50000).
• Ask AI to generate equivalent Pandas code.
• Test the generated code on a sample DataFrame.
Expected Output:
• Equivalent Pandas query that retrieves the correct subset of
data.'''
'''# Sample SQL query
SELECT name, salary FROM employees WHERE salary > 50000;
'''
# Equivalent Pandas code
import pandas as pd
# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],  
    'salary': [60000, 45000, 70000, 30000]
}
df = pd.DataFrame(data)
# Filtering the DataFrame based on the condition
result = df[df['salary'] > 50000][['name', 'salary']]   

'''Task 5 – Real-Time Application: Algorithm Translation Across
Languages
Scenario:
A company maintains algorithms written in different programming
languages.
Examples:
• Converting a Python searching algorithm into C
• Translating a Java sorting program into JavaScript
Instructions:
• Use AI to translate a selected algorithm between two
programming languages
• Execute and test both versions
• Document translation challenges such as:
o Syntax differences
o Library support
o Memory management'''
# Python code for a simple linear search algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Testing the linear_search function
test_array = [5, 3, 2, 8, 1]
target_value = 2
result = linear_search(test_array, target_value)
print(f"Element {target_value} found at index: {result}")
'''// C code for a simple linear search algorithm
#include <stdio.h>
int linear_search(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
int main() {
    int arr[] = {5, 3, 2, 8, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 2;
    int result = linear_search(arr, n, target);
    if (result != -1) {
        printf("Element %d found at index: %d\n", target, result);
    } else {
        printf("Element %d not found in the array.\n", target);
    }
    return 0;
}'''
