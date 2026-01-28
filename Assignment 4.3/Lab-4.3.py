'''Write a Python function that accepts a year as input and checks whether it is a leap year.
Constraints:

Use correct leap year rules (divisible by 4, century years divisible by 400).

Validate the input to ensure it is a positive integer year.

Return or print an appropriate result indicating whether the year is a leap year.

Keep the code simple and readable.'''
def is_leap_year(year):
    if not isinstance(year, int) or year <= 0:
        print("Invalid input: Please enter a positive integer year.")
        return
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is Not a Leap Year")
# Example usage:
is_leap_year(2020)  # 2020 is a Leap Year
is_leap_year(1900)  # 1900 is Not a Leap Year
is_leap_year(2000)  # 2000 is a Leap Year
is_leap_year(-2020) # Invalid input: Please enter a positive integer year.

'''Write a Python function that converts a given value in centimeters to inches using the correct formula.

Example:
Input: 10 cm → Output: 3.94 inches

Constraints:

Use the standard conversion (1 inch = 2.54 cm).

Return or print the converted value rounded to two decimal places.

Keep the function simple and readable.

Include a few sample test cases with outputs'''

def cm_to_inches(cm):
    if not isinstance(cm, (int, float)) or cm < 0:
        print("Invalid input: Please enter a positive number.")
        return
    inches = cm / 2.54
    print(f"{cm} cm is equal to {inches:.2f} inches")

# Example usage:
cm_to_inches(10)   # 10 cm is equal to 3.94 inches
cm_to_inches(25.4) # 25.4 cm is equal to 10.00 inches
cm_to_inches(-5)   # Invalid input: Please enter a positive number.
cm_to_inches(0)    # 0 cm is equal to 0.00 inches


'''Write a Python function that takes a full name as input and formats it as Last, First.

Examples:
Input: John Smith → Output: Smith, John
Input: Anita Rao → Output: Rao, Anita

Instructions & Constraints:

Assume the input contains exactly two words (first name and last name).

Output must strictly follow the format shown in the examples.

Keep the function simple, clean, and readable.

Include sample inputs and outputs'''
def format_name(full_name):
    if not isinstance(full_name, str):
        print("Invalid input: Please enter a valid full name.")
        return
    names = full_name.split()
    if len(names) != 2:
        print("Invalid input: Please enter exactly two names (first and last).")
        return
    first_name, last_name = names
    print(f"{last_name}, {first_name}")
# Example usage:
format_name("John Smith")  # Smith, John
format_name("Anita Rao")   # Rao, Anita
format_name("SingleName")   # Invalid input: Please enter exactly two names (first and last).
format_name(12345)         # Invalid input: Please enter a valid full name.

'''Write a Python function that takes a string as input and counts the number of vowels in it.
Constraints:

Consider both uppercase and lowercase vowels.

Ignore non-alphabetic characters.

Return the total vowel count'''
def count_vowels(input_string):
    if not isinstance(input_string, str):
        print("Invalid input: Please enter a valid string.")
        return
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    print(f"Number of vowels: {count}")
# Example usage:
count_vowels("Hello World")      # Number of vowels: 3
count_vowels("Python Programming") # Number of vowels: 4

'''Write a Python function that counts vowels in a string.

Examples:
Input: 'hello' → Output: 2
Input: 'PYTHON' → Output: 1
Input: 'ChatGPT' → Output: 2

Constraints:

Handle uppercase and lowercase letters.

Ignore non-alphabetic characters.

Return the vowel count.'''
def count_vowels(input_string):
    if not isinstance(input_string, str):
        print("Invalid input: Please enter a valid string.")
        return
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    print(f"Number of vowels: {count}")
# Example usage:
count_vowels("hello")      # Number of vowels: 2
count_vowels("PYTHON")     # Number of vowels: 1



'''Write a Python function that reads a .txt file and returns the number of lines.

Examples:
File content:
Hello
World
→ Output: 2

File content:
Only one line
→ Output: 1

Constraints:

Accept file path as input

Handle empty files

Use proper file handling'''
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines: {len(lines)}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Example usage:
count_lines_in_file('example.txt')  # Number of lines: 2
count_lines_in_file('single_line.txt')  # Number of lines: 1
count_lines_in_file('non_existent.txt')  # File not found. Please check the file path.
