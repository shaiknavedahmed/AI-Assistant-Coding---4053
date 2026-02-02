#Task 1
'''Generate code to fetch weather data securely without exposing API keys in the code.'''
'''import os
import requests

API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Set WEATHER_API_KEY as an environment variable.")

CITY = "London"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(URL, params=params)
data = response.json()

print(data)
'''
'''import requests

CITY = "London"
LAT = 51.5072
LON = -0.1276

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": LAT,
    "longitude": LON,
    "current_weather": True
}'''

'''response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
    print({
        "city": CITY,
        "temperature": f"{weather['temperature']}°C",
        "windspeed": weather["windspeed"]
    })
else:
    print("API error")'''

#Task 2
'''Generate a Python script that stores user data (name, email, password) into a file.
Then analyze the script to identify any privacy or security risks, especially related to storing sensitive data.
Finally, provide a revised version of the program that securely stores passwords using encryption or hashing instead of plain text.'''

'''#Insecure version
def store_user_data(name, email, password):
    with open("users.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Password: {password}\n")

name = input("Enter name: ")
email = input("Enter email: ")
password = input("Enter password: ")

store_user_data(name, email, password)
print("User data stored successfully.")

#Revised secure version
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def store_user_data(name, email, password):
    hashed_password = hash_password(password)
    with open("users_secure.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Password Hash: {hashed_password}\n")

name = input("Enter name: ")
email = input("Enter email: ")
password = input("Enter password: ")

store_user_data(name, email, password)
print("User data stored securely.")'''


#Task 3
'''Generate a Python function that checks whether a given number is an Armstrong number.
Include clear comments in the code and provide a line-by-line explanation of how the algorithm works.
Ensure the logic is correct, easy to understand, and matches the explanation exactly.'''
'''def is_armstrong_number(num):
    """
    Check if a number is an Armstrong number.
    
    An Armstrong number is a number that is equal to the sum of its own digits 
    each raised to the power of the number of digits.
    
    For example, 153 is an Armstrong number because:
    1^3 + 5^3 + 3^3 = 153
    """
    # Convert the number to string to easily iterate over digits
    str_num = str(num)
    
    # Get the number of digits in the number
    num_digits = len(str_num)
    
    # Initialize sum to store the sum of digits raised to the power of num_digits
    sum_of_powers = 0
    
    # Iterate over each digit in the string representation of the number
    for digit in str_num:
        # Convert digit back to integer and raise it to the power of num_digits
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the calculated sum is equal to the original number
    return sum_of_powers == num
# Example usage
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
number = 123
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
'''
#Task 4
'''Generate Python implementations of QuickSort and BubbleSort.
Include clear, step-by-step comments in the code explaining how each algorithm works.
After the code, provide a transparent comparison explaining the differences in their logic, efficiency, and use cases.'''
def quicksort(arr):
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (here, the last element)
    pivot = arr[-1]
    # Elements smaller than or equal to the pivot
    left = []
    # Elements greater than the pivot
    right = []
    # Compare each element (except pivot) with the pivot
    for element in arr[:-1]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)
    # Recursively apply QuickSort to left and right parts
    return quicksort(left) + [pivot] + quicksort(right)

def bubblesort(arr):
    n = len(arr)

    # Outer loop controls number of passes
    for i in range(n):
        # Inner loop compares adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Sample input
data = [64, 34, 25, 12, 22, 11, 90]
# Outputs
print("Original List:", data)
print("QuickSort Output:", quicksort(data))
print("BubbleSort Output:", bubblesort(data.copy()))

#Task 5
'''Generate a simple product recommendation system in Python.
The system should recommend products to users and also provide a clear explanation or reason for each recommendation.
Ensure that the recommendation logic is transparent, easy to understand, and that each suggestion includes why it was recommended.'''
def recommend_products(user_interest):
    # Product database with categories
    products = {
        "Smartphone": "Electronics",
        "Laptop": "Electronics",
        "Headphones": "Electronics",
        "Running Shoes": "Sports",
        "Yoga Mat": "Sports",
        "Dumbbells": "Sports",
        "Novel Book": "Books",
        "Textbook": "Books"
    }

    recommendations = []

    # Check products that match user's interest
    for product, category in products.items():
        if category.lower() == user_interest.lower():
            # Add product with explanation
            recommendations.append(
                (product, f"Recommended because you are interested in {category}.")
            )

    return recommendations


# Sample usage
interest = input("Enter your interest (Electronics / Sports / Books): ")
results = recommend_products(interest)

if results:
    for item, reason in results:
        print(f"{item} → {reason}")
else:
    print("No recommendations found for your interest.")
