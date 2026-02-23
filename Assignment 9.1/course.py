#Lab 9.1
#Task 5

"""
course.py

Simple course management module for adding, removing,
and retrieving course information.
"""

# In-memory storage for courses
courses = {}


def add_course(course_id, name, credits):
    """Add a course with ID, name, and credit value."""
    courses[course_id] = {
        "name": name,
        "credits": credits
    }
    return True


def remove_course(course_id):
    """Remove a course by its ID. Returns True if removed, False if not found."""
    return courses.pop(course_id, None) is not None


def get_course(course_id):
    """Retrieve course details by ID. Returns course info or None if not found."""
    return courses.get(course_id)