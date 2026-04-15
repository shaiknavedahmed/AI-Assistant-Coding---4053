// class Student:
//     def __init__(self, name, marks):
//         self.__name = name          # private attribute
//         self.__marks = marks        # private attribute

//     # Getter
//     def get_name(self):
//         return self.__name

//     def get_marks(self):
//         return self.__marks

//     # Setter
//     def set_marks(self, marks):
//         if marks >= 0:
//             self.__marks = marks

//     # Derived method
//     def calculate_grade(self):
//         if self.__marks >= 90:
//             return "A"
//         elif self.__marks >= 75:
//             return "B"
//         elif self.__marks >= 50:
//             return "C"
//         else:
//             return "Fail"


// # Test
// s = Student("Naved", 85)
// print(s.get_name(), s.get_marks(), s.calculate_grade())
// #include <iostream>
// using namespace std;

// class Student {
// private:
//     string name;
//     int marks;

// public:
//     // Constructor
//     Student(string n, int m) {
//         name = n;
//         marks = m;
//     }

//     // Getter
//     string getName() {
//         return name;
//     }

//     int getMarks() {
//         return marks;
//     }

//     // Setter
//     void setMarks(int m) {
//         if (m >= 0) {
//             marks = m;
//         }
//     }

//     // Derived method
//     string calculateGrade() {
//         if (marks >= 90)
//             return "A";
//         else if (marks >= 75)
//             return "B";
//         else if (marks >= 50)
//             return "C";
//         else
//             return "Fail";
//     }
// };

// int main() {
//     Student s("Naved", 85);
//     cout << s.getName() << " " << s.getMarks() << " " << s.calculateGrade();
//     return 0;
// }


