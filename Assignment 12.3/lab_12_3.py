#Task 1
#Sorting Student Records for Placement Drive 
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}"   
def sort_students(students):
    return sorted(students, key=lambda student: student.marks, reverse=True)    
# Sample student records
students = [
    Student("Alice", 101, 85),
    Student("Bob", 102, 92),
    Student("Charlie", 103, 78),
    Student("David", 104, 90),
    Student("Eve", 105, 88)
]
# Sorting students based on marks
sorted_students = sort_students(students)
# Displaying sorted student records
print("Sorted Student Records for Placement Drive:")
for student in sorted_students:
    print(student)  

#Explanation:
#1. We define a class `Student` with an initializer that takes the student's name, roll number, and marks. The `__str__` method is overridden to provide a string representation of the student object.
#2. The `sort_students` function takes a list of student objects and sorts them based on their marks in descending order using the `sorted` function and a lambda function as the key.
#3. We create a sample list of student records and call the `sort_students` function to sort them.
#4. Finally, we print the sorted student records to the console.    

#Task 2
#Implementing Bubble Sort with AI Comments
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Sample array to be sorted
arr = [64, 34, 25, 12, 22, 11, 90]
# Sorting the array using bubble sort   
sorted_arr = bubble_sort(arr)
# Displaying the sorted array
print("Sorted array is:", sorted_arr)   

#Explanation:
#1. The `bubble_sort` function takes an array as input and sorts it in ascending order using the bubble sort algorithm.
#2. The outer loop iterates through each element in the array, while the inner loop compares adjacent elements and swaps them if they are in the wrong order.
#3. The process is repeated until the entire array is sorted, with the largest elements "bubbling" to the end of the array in each iteration.
#4. Finally, we print the sorted array to the console.

#Task 3
#Quick Sort and Merge Sort Comparison
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
# Sample array to be sorted
arr_quick = [10, 7, 8, 9, 1, 5]
arr_merge = [38, 27, 43, 3, 9, 82, 10]
# Sorting the array using quick sort
sorted_quick = quick_sort(arr_quick)        
# Sorting the array using merge sort
merge_sort(arr_merge)
# Displaying the sorted arrays
print("Sorted array using Quick Sort is:", sorted_quick)
print("Sorted array using Merge Sort is:", arr_merge)

#Explanation:
#1. The `quick_sort` function implements the quick sort algorithm, which uses a pivot to partition the array into two sub-arrays and recursively sorts them.        
#2. The `merge_sort` function implements the merge sort algorithm, which divides the array into halves, recursively sorts them, and then merges the sorted halves back together.
#3. We create sample arrays for both sorting algorithms and call the respective functions to sort them.
#4. Finally, we print the sorted arrays to the console for comparison.

#Task 4
#Real-Time Application – Inventory Management System
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}"
class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
    def sort_inventory(self):
        self.inventory.sort(key=lambda item: item.quantity, reverse=True)
    def display_inventory(self):
        for item in self.inventory:
            print(item)
# Sample inventory items
item1 = InventoryItem("Laptop", 10)
item2 = InventoryItem("Smartphone", 25) 
item3 = InventoryItem("Tablet", 15)
# Creating an instance of InventoryManagementSystem
inventory_system = InventoryManagementSystem()
# Adding items to the inventory
inventory_system.add_item(item1)
inventory_system.add_item(item2)
inventory_system.add_item(item3)
# Sorting the inventory based on quantity
inventory_system.sort_inventory()
# Displaying the sorted inventory
print("Sorted Inventory:")
inventory_system.display_inventory()

#Explanation:
#1. We define a class `InventoryItem` to represent each item in the inventory, with attributes for the item's name and quantity. The `__str__` method provides a string representation of the item.
#2. The `InventoryManagementSystem` class manages the inventory, allowing us to add items, sort the inventory based on quantity, and display the inventory.
#3. We create sample inventory items and add them to the inventory system.
#4. We call the `sort_inventory` method to sort the items based on their quantity in descending order and then display the sorted inventory

#Task 5
#Real-Time Stock Data Sorting & Searching
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
    def __str__(self):
        return f"Stock: {self.symbol}, Price: {self.price}"
def sort_stocks(stocks):
    return sorted(stocks, key=lambda stock: stock.price, reverse=True)
def search_stock(stocks, symbol):
    for stock in stocks:
        if stock.symbol == symbol:
            return stock
    return None
# Sample stock data
stock1 = Stock("AAPL", 150)
stock2 = Stock("GOOGL", 2800)
stock3 = Stock("AMZN", 3400)
# List of stocks
stocks = [stock1, stock2, stock3]
# Sorting stocks based on price 
sorted_stocks = sort_stocks(stocks)
# Displaying sorted stocks
print("Sorted Stocks by Price:")
for stock in sorted_stocks:
    print(stock)
# Searching for a specific stock
search_symbol = "GOOGL"
found_stock = search_stock(stocks, search_symbol)
if found_stock:
    print(f"\nStock found: {found_stock}")
else:
    print(f"\nStock with symbol {search_symbol} not found.")
    
#Explanation:
#1. We define a class `Stock` to represent each stock, with attributes for the stock symbol and price. The `__str__` method provides a string representation of the stock.  
#2. The `sort_stocks` function sorts a list of stock objects based on their price in descending order using the `sorted` function and a lambda function as the key.
#3. The `search_stock` function searches for a stock in the list based on its symbol and returns the stock object if found, or `None` if not found.
#4. We create sample stock data and call the `sort_stocks` function to sort the stocks by price, and then display the sorted stocks.
#5. We also call the `search_stock` function to search for a specific stock symbol and display the result.