"""
Module-level docstring.

This module encapsulates the School class, which represents an educational institution
where students attend classes and receive instruction from teachers.
"""


from student import Student
from course import Course


class School:
    """School class, do not change."""

    def __init__(self, name):
        """Initialize a new school."""
        self.name = name
        self.students = []
        self.courses = []
        self.student_id_counter = 1

    def add_course(self, course: Course):
        """Add a course to the school."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        """Add a student to the school."""
        if student not in self.students:
            student.set_id(self.student_id_counter)
            self.student_id_counter += 1
            self.students.append(student)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """Add a grade for a student to the classes and students personal grade list."""
        if student in self.students:
            if course in self.courses:
                student.add_grade(course, grade)
                course.add_grade(student, grade)

    def get_students(self):
        """Return list of students."""
        return self.students

    def get_courses(self):
        """Return list of courses."""
        return self.courses

    def get_students_ordered_by_average_grade(self):
        """Return a list of students ordered by their average grade in descending order."""
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)