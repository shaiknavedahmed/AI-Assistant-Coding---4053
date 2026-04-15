// import requests

// def fetch_users():
//     try:
//         response = requests.get("https://jsonplaceholder.typicode.com/users")
//         response.raise_for_status()  # raises error for bad status
        
//         data = response.json()
        
//         for user in data:
//             print(user["name"])
    
//     except requests.exceptions.RequestException as e:
//         print("Error:", e)

// fetch_users()

// Give the above code in JavaScript using fetch API

async function fetchUsers() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/users");

        if (!response.ok) {
            throw new Error("HTTP error! Status: " + response.status);
        }

        const data = await response.json();

        data.forEach(user => {
            console.log(user.name);
        });

    } catch (error) {
        console.error("Error:", error.message);
    }
}

fetchUsers();