--Task1
--Create schema and queries for a Hospital Management System. Tables: Doctors, Patients, Appointments. queries: List all appointments for a specific doctor, Retrieve patient history by patient ID, Count total patients treated by each doctor. Output: Normalized schema and SQL queries with joins.

DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Doctors;

CREATE TABLE Doctors (
    doctor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialization TEXT,
    UNIQUE(name)
);

CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dob DATE,
    UNIQUE(name, dob)
);

CREATE TABLE Appointments (
    appointment_id INTEGER PRIMARY KEY,
    doctor_id INTEGER,
    patient_id INTEGER,
    appointment_date TEXT,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

INSERT INTO Doctors VALUES (1, 'Dr. Smith', 'Cardiology');
INSERT INTO Doctors VALUES (2, 'Dr. John', 'Neurology');

INSERT INTO Patients VALUES (1, 'Naved', '2004-01-01');
INSERT INTO Patients VALUES (2, 'Rahul', '2003-05-10');

INSERT INTO Appointments VALUES (1, 1, 1, '2025-03-20');
INSERT INTO Appointments VALUES (2, 1, 2, '2025-03-21');
INSERT INTO Appointments VALUES (3, 2, 1, '2025-03-22');

--Appointments for a specific doctor
SELECT a.*
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE d.name = 'Dr. Smith';
--Patient history
SELECT a.*
FROM Appointments a
WHERE a.patient_id = 1;
--Total patients per doctor
SELECT d.name, COUNT(DISTINCT a.patient_id) AS total_patients
FROM Doctors d
JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.name;

SELECT * FROM Doctors;
SELECT * FROM Patients;
SELECT * FROM Appointments;

--Explanation:
--The schema is normalized to avoid redundancy. Doctors and Patients have unique constraints to prevent duplicate entries. Appointments link doctors and patients with foreign keys. Queries utilize joins to retrieve relevant data efficiently, ensuring accurate results while maintaining data integrity.

--Task2
--Real-Time Application: Online Shopping Database. Tables: Users, Products, Orders, OrderDetails.
--Generate queries to: Retrieve all orders by a user, Find the most purchased product, Calculate total revenue in a given month, AI should also suggest normalization improvements and query optimization.
--Expected Output: Complete schema with relationships + SQL queries for analytics.
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL CHECK(price > 0)
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    order_date DATE,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

CREATE TABLE OrderDetails (
    order_detail_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER CHECK(quantity > 0),
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

INSERT INTO Users VALUES (1, 'Naved', 'naved@gmail.com');

INSERT INTO Products VALUES (1, 'Laptop', 50000);
INSERT INTO Products VALUES (2, 'Mouse', 500);

INSERT INTO Orders VALUES (1, 1, '2026-03-10');

INSERT INTO OrderDetails VALUES (1, 1, 1, 1);
INSERT INTO OrderDetails VALUES (2, 1, 2, 2);

--Orders by a user
SELECT o.*
FROM Orders o
JOIN Users u ON o.user_id = u.user_id
WHERE u.name = 'Naved';
--Most purchased product
SELECT p.name, SUM(od.quantity) AS total_sold
FROM OrderDetails od
JOIN Products p ON od.product_id = p.product_id
GROUP BY p.name
ORDER BY total_sold DESC
LIMIT 1;
--Monthly revenue
SELECT SUM(p.price * od.quantity) AS revenue
FROM OrderDetails od
JOIN Orders o ON od.order_id = o.order_id
JOIN Products p ON od.product_id = p.product_id
WHERE strftime('%Y-%m', o.order_date) = '2026-03';

SELECT * FROM Users;
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM OrderDetails;

--Explanation:
--The schema is designed to maintain data integrity and avoid redundancy. Users and Products have unique constraints to prevent duplicates. Orders and OrderDetails link users and products with foreign keys. Queries are optimized using joins to efficiently retrieve relevant data, ensuring accurate analytics while maintaining performance. Normalization ensures that data is stored in a structured manner, reducing redundancy and improving data integrity.

--Task3
--Library Database
--Task: Design schema for a Library Management System.
--Tables: Books, Members, Loans.
--Generate queries: Retrieve all books currently issued, Find overdue books (loan date > 30 days), Count number of books loaned by each member.
--Expected Output: Schema + SQL queries demonstrating joins and conditions.
CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT
);

CREATE TABLE Members (
    member_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Loans (
    loan_id INTEGER PRIMARY KEY,
    book_id INTEGER,
    member_id INTEGER,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY(book_id) REFERENCES Books(book_id),
    FOREIGN KEY(member_id) REFERENCES Members(member_id)
);

INSERT INTO Books VALUES (1, 'DBMS', 'Author1');
INSERT INTO Books VALUES (2, 'OS', 'Author2');

INSERT INTO Members VALUES (1, 'Naved');

INSERT INTO Loans VALUES (1, 1, 1, '2026-02-01', NULL);

--Books currently issued
SELECT b.title, m.name
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL;
--Overdue books (>30 days)
SELECT b.title, m.name
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE julianday('now') - julianday(l.loan_date) > 30
AND l.return_date IS NULL;
--Books per member
SELECT m.name, COUNT(l.book_id) AS total_books
FROM Members m
JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.name;

SELECT * FROM Books;
SELECT * FROM Members;
SELECT * FROM Loans;

--Explanation:
--The schema is designed to maintain data integrity and avoid redundancy. Books and Members have unique constraints to prevent duplicates. Loans link books and members with foreign keys, allowing for efficient tracking of issued books. Queries utilize joins to retrieve relevant data based on conditions, ensuring accurate results while maintaining performance. The use of conditions in queries allows for filtering data effectively, such as identifying overdue books and counting the number of books loaned by each member. 

--Task4
--Optimize Queries
--Instructions: Optimize inefficient queries using joins, indexes, or reducing subqueries, Test optimized queries for correctness.
--Starter Code Example:
-- Original query
SELECT * FROM Books WHERE author_id IN (SELECT author_id FROM
Authors WHERE country='UK');
-- Optimized query
SELECT b.*
FROM Books b
JOIN Authors a ON b.author_id = a.author_id
WHERE a.country = 'UK';

-- Original query
SELECT * FROM Orders WHERE user_id IN (SELECT user_id FROM Users WHERE email LIKE '%@example.com');
-- Optimized query
SELECT o.*
FROM Orders o
JOIN Users u ON o.user_id = u.user_id
WHERE u.email LIKE '%@example.com';

--Explanation:
--The original queries use subqueries which can be inefficient, especially if the subquery returns a large number of results. The optimized queries utilize joins, which are generally more efficient for retrieving related data. By joining the relevant tables directly, we can filter results more efficiently and reduce the overhead associated with subqueries. Additionally, ensuring that appropriate indexes are in place on the columns used in joins and where conditions can further enhance query performance. Testing the optimized queries for correctness ensures that they return the expected results while improving efficiency.    

--Task5
--University Course Registration: SR University needs a course registration system for students enrolling in different courses under faculty supervision.
--Define relationships: Each student can register for multiple courses, Each course is taught by a faculty member.
--Write SQL queries to: List all students enrolled in a specific course, Find faculty members teaching more than 2 courses, Retrieve courses with the highest number of registrations.

DROP TABLE IF EXISTS Registrations;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Faculty (
    faculty_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    faculty_id INTEGER,
    FOREIGN KEY(faculty_id) REFERENCES Faculty(faculty_id)
);

CREATE TABLE Registrations (
    reg_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
);

INSERT INTO Students VALUES (1, 'Naved');
INSERT INTO Students VALUES (2, 'Rahul');

INSERT INTO Faculty VALUES (1, 'Prof A');

INSERT INTO Courses VALUES (1, 'DBMS', 1);
INSERT INTO Courses VALUES (2, 'OS', 1);
INSERT INTO Courses VALUES (3, 'CN', 1);

INSERT INTO Registrations VALUES (1, 1, 1);
INSERT INTO Registrations VALUES (2, 2, 1);
INSERT INTO Registrations VALUES (3, 1, 2);

--Students in a course
SELECT s.name
FROM Registrations r
JOIN Students s ON r.student_id = s.student_id
WHERE r.course_id = 1;
--Faculty teaching >2 courses
SELECT f.name, COUNT(c.course_id) AS course_count
FROM Faculty f
JOIN Courses c ON f.faculty_id = c.faculty_id
GROUP BY f.name
HAVING course_count > 2;
--Courses with highest registrations
SELECT c.course_name, COUNT(r.student_id) AS total_registrations
FROM Courses c
JOIN Registrations r ON c.course_id = r.course_id
GROUP BY c.course_name
ORDER BY total_registrations DESC
LIMIT 1;

SELECT * FROM Students;
SELECT * FROM Faculty;
SELECT * FROM Courses;
SELECT * FROM Registrations;

--Explanation:
--The schema is designed to maintain data integrity and avoid redundancy. Students and Faculty have unique constraints to prevent duplicates. Courses link to Faculty with a foreign key, and Registrations link Students and Courses with foreign keys, allowing for efficient tracking of course enrollments. Queries utilize joins to retrieve relevant data based on conditions, ensuring accurate results while maintaining performance. The use of GROUP BY and HAVING clauses allows for aggregation and filtering of results, such as identifying faculty members teaching more than 2 courses and retrieving courses with the highest number of registrations.
