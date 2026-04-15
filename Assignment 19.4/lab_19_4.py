#Task 1
'''
function averageAbove50(arr) {
    const filtered = arr.filter(num => num > 50);
    
    if (filtered.length === 0) return 0;

    const sum = filtered.reduce((acc, num) => acc + num, 0);
    return sum / filtered.length;
}

// Sample Test
const data = [30, 60, 80, 45, 90];
console.log(averageAbove50(data)); // Output: 76.666...
'''
#give python code for the above function
def average_above_50(arr):
    filtered = [num for num in arr if num > 50]
    
    if not filtered:
        return 0
    
    return sum(filtered) / len(filtered)

# Sample Test
data = [30, 60, 80, 45, 90]
print(average_above_50(data))  # Output: 76.666...


#Task 3

import requests

def fetch_users():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()  # raises error for bad status
        
        data = response.json()
        
        for user in data:
            print(user["name"])
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)

fetch_users()
