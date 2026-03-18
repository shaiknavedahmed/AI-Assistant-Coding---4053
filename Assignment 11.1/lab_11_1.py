#Task 1#Use AI to generate a Stack class with push, pop, peek, and is_empty methods. A functional stack implementation with all required methods and docstrings.
class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack. Raises an exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it. Raises an exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.items) == 0
# Example usage
stack = Stack()
stack.push(1)   
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.is_empty())  # Output: False

#Explanation: The Stack class is implemented with an internal list to hold the stack items. The push method adds an item to the top of the stack, while the pop method removes and returns the top item, checking for emptiness before popping. The peek method allows viewing the top item without removing it, also checking for emptiness. The is_empty method checks if the stack has any items. The example usage demonstrates how to use the Stack class. 

#Task 2
#to implement a Queue using Python lists.FIFO-based queue class with enqueue, dequeue, peek, and size methods.
class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue. Raises an exception if the queue is empty."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the item at the front of the queue without removing it. Raises an exception if the queue is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.items) == 0
# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())  # Output: 1

#Explanation: The Queue class is implemented using a list to hold the queue items. The enqueue method adds an item to the end of the queue, while the dequeue method removes and returns the front item, checking for emptiness before dequeuing. The peek method allows viewing the front item without removing it, also checking for emptiness. The size method returns the number of items in the queue, and the is_empty method checks if the queue has any items. The example usage demonstrates how to use the Queue class.   

#Task 3
#Use AI to generate a Singly Linked List with insert and display methods. A working linked list implementation with clear method documentation.
class Node:
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def insert(self, data):
        """Insert a new node with the given data at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        """Display the contents of the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')
# Example usage
linked_list = SinglyLinkedList()
linked_list.insert(1)       
linked_list.insert(2)
linked_list.insert(3)
linked_list.display()  # Output: 1 -> 2 -> 3 -> None

#Explanation: The Node class represents a single node in the linked list, containing data and a pointer to the next node. The SinglyLinkedList class manages the linked list, allowing for insertion of new nodes at the end and displaying the contents of the list. The insert method creates a new node and adds it to the end of the list, while the display method traverses the list and prints each node's data in a readable format. The example usage demonstrates how to use the SinglyLinkedList class.  

#Task 4
#Use AI to create a BST with insert and in-order traversal methods. BST implementation with recursive insert and traversal methods.
class TreeNode:
    def __init__(self, key):
        """Initialize a tree node with a key and pointers to left and right children."""
        self.left = None
        self.right = None
        self.val = key
class BinarySearchTree:
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root = None

    def insert(self, key):
        """Insert a new key into the binary search tree."""
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """Helper method to insert a new key recursively."""
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def in_order_traversal(self):
        """Perform in-order traversal of the binary search tree and return a list of keys."""
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        """Helper method to perform in-order traversal recursively."""
        res = []
        if node:
            res = self._in_order_recursive(node.left)
            res.append(node.val)
            res = res + self._in_order_recursive(node.right)
        return res
# Example usage 
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
print(bst.in_order_traversal())  # Output: [3, 5, 7]

#Explanation: The TreeNode class represents a node in the binary search tree, containing a key and pointers to left and right children. The BinarySearchTree class manages the tree structure, allowing for insertion of new keys and performing in-order traversal. The insert method adds a new key to the tree, while the in_order_traversal method returns a list of keys in sorted order by traversing the tree recursively. The example usage demonstrates how to use the BinarySearchTree class.

#Task 5
#Use AI to implement a hash table with basic insert, search, and delete methods. Collision handling using chaining, with well-commented methods.
class HashTable:
    def __init__(self, size=10):
        """Initialize a hash table with a specified size and an empty list for chaining."""
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Generate a hash for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table. Handles collisions using chaining."""
        index = self._hash(key)
        # Check if the key already exists and update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        # If the key does not exist, add a new key-value pair
        self.table[index].append((key, value))

    def search(self, key):
        """Search for a value by its key in the hash table. Returns the value or None if not found."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value if the key is found
        return None  # Return None if the key is not found

    def delete(self, key):
        """Delete a key-value pair from the hash table. Returns True if deleted, False if not found."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair
                return True  # Return True if deletion was successful
        return False  # Return False if the key was not found
# Example usage
hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
print(hash_table.search("name"))  # Output: Alice
print(hash_table.delete("age"))    # Output: True
print(hash_table.search("age"))    # Output: None

#Explanation: The HashTable class implements a hash table with chaining for collision resolution. The _hash method generates a hash index for a given key. The insert method adds a key-value pair to the appropriate index, updating existing keys if necessary. The search method retrieves the value associated with a key, returning None if the key is not found. The delete method removes a key-value pair from the hash table, returning True if the deletion was successful and False if the key was not found. The example usage demonstrates how to use the HashTable class.

#Task 6
#Use AI to implement a graph using an adjacency list. Graph with methods to add vertices, add edges, and display connections.
class Graph:
    def __init__(self):
        """Initialize an empty graph with an adjacency list."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph. If the vertex already exists, do nothing."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices in the graph. If the vertices do not exist, they will be added."""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)  # For undirected graph

    def display(self):
        """Display the adjacency list of the graph."""
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {', '.join(edges)}")
# Example usage
graph = Graph()
graph.add_edge("A", "B")    
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.display()

#Explanation: The Graph class uses an adjacency list to represent the graph structure. The add_vertex method adds a vertex to the graph if it does not already exist. The add_edge method creates an edge between two vertices, adding them to each other's adjacency list for an undirected graph. The display method prints the adjacency list, showing each vertex and its connected vertices. The example usage demonstrates how to create a graph, add edges, and display the connections.

#Task 7
#to implement a priority queue using Python’s heapq module. Implementation with enqueue (priority), dequeue (highest priority), and display methods.
import heapq
class PriorityQueue:
    def __init__(self):
        """Initialize an empty priority queue using a heap."""
        self.elements = []

    def enqueue(self, item, priority):
        """Add an item to the priority queue with a given priority."""
        heapq.heappush(self.elements, (priority, item))

    def dequeue(self):
        """Remove and return the item with the highest priority (lowest priority number). Raises an exception if the queue is empty."""
        if not self.elements:
            raise IndexError("Dequeue from an empty priority queue")
        return heapq.heappop(self.elements)[1]  # Return the item, not the priority

    def display(self):
        """Display the contents of the priority queue."""
        print("Priority Queue Contents:")
        for priority, item in sorted(self.elements):
            print(f"Priority: {priority}, Item: {item}")
# Example usage
pq = PriorityQueue()
pq.enqueue("Task A", 2)
pq.enqueue("Task B", 1) 
pq.enqueue("Task C", 3)
pq.display()
print(pq.dequeue())  # Output: Task B (highest priority)

#Explanation: The PriorityQueue class uses the heapq module to manage a priority queue. The enqueue method adds an item with a specified priority to the queue, while the dequeue method removes and returns the item with the highest priority (the lowest priority number). The display method shows the contents of the priority queue sorted by priority. The example usage demonstrates how to add tasks with different priorities, display the queue, and dequeue the highest priority task.

#Task 8
#Use AI to implement a double-ended queue using collections.deque.  Insert and remove from both ends with docstrings.
from collections import deque
class DoubleEndedQueue:
    def __init__(self):
        """Initialize an empty double-ended queue."""
        self.deque = deque()

    def insert_front(self, item):
        """Insert an item at the front of the double-ended queue."""
        self.deque.appendleft(item)

    def insert_rear(self, item):
        """Insert an item at the rear of the double-ended queue."""
        self.deque.append(item)

    def remove_front(self):
        """Remove and return the item from the front of the double-ended queue. Raises an exception if the deque is empty."""
        if not self.deque:
            raise IndexError("Remove from an empty deque")
        return self.deque.popleft()

    def remove_rear(self):
        """Remove and return the item from the rear of the double-ended queue. Raises an exception if the deque is empty."""
        if not self.deque:
            raise IndexError("Remove from an empty deque")
        return self.deque.pop()

    def display(self):
        """Display the contents of the double-ended queue."""
        print("Double-Ended Queue Contents:")
        print(list(self.deque))
# Example usage
deque = DoubleEndedQueue()
deque.insert_rear("Task A")
deque.insert_rear("Task B")
deque.insert_front("Task C")
deque.display()  # Output: ['Task C', 'Task A', 'Task B']
print(deque.remove_front())  # Output: Task C
print(deque.remove_rear())   # Output: Task B

#Explanation: The DoubleEndedQueue class uses the collections.deque to implement a double-ended queue. The insert_front and insert_rear methods allow adding items to the front and rear of the deque, respectively. The remove_front and remove_rear methods remove and return items from the front and rear, checking for emptiness before attempting to remove. The display method shows the current contents of the deque. The example usage demonstrates how to use the DoubleEndedQueue class to manage tasks in a double-ended queue.

#Task 9
#Real-Time Application Challenge – Choose the Right Data Structure
from collections import deque

class CafeteriaQueue:
    """
    A simple queue system to manage cafeteria orders.
    Students are served in FIFO (First In First Out) order.
    """

    def __init__(self):
        self.queue = deque()

    def add_order(self, student_name):
        """Add a student order to the queue."""
        self.queue.append(student_name)
        print(f"{student_name} added to the queue.")

    def serve_order(self):
        """Serve the first student in the queue."""
        if self.queue:
            served = self.queue.popleft()
            print(f"Serving {served}.")
        else:
            print("No orders in queue.")

    def display_queue(self):
        """Display current queue."""
        print("Current Queue:", list(self.queue))


#Sample Usage
cq = CafeteriaQueue()

cq.add_order("Naved")
cq.add_order("Rahul")
cq.add_order("Aisha")

cq.display_queue()

cq.serve_order()
cq.display_queue()

cq.serve_order()
cq.serve_order()
cq.serve_order()  # empty case

#Explanation: The CafeteriaQueue class uses a deque to manage student orders in a FIFO manner. The add_order method adds a student's name to the end of the queue, while the serve_order method removes and serves the first student in the queue. The display_queue method shows the current state of the queue. The sample usage demonstrates how to add orders, display the queue, and serve students, including handling the case when the queue is empty.
