"""
Module-level docstring.

This module contains the definition of the Student class. which represents a person
who attends school.
"""


from course import Course


class Student:
    """Student class, do not change."""

    def __init__(self, name: str, id=None):
        """Initiate new student."""
        self.name = name
        self.id = id
        self.grades = []

    def set_id(self, id: int):
        """Set student ID."""
        if self.id is None:
            self.id = id

    def get_id(self):
        """Return student ID."""
        return self.id

    def get_grades(self):
        """Return students grades."""
        return self.grades

    def get_average_grade(self):
        """Get the average grade for this student."""
        if len(self.grades) == 0:
            return -1
        else:
            total_grade = sum(grade for _, grade in self.grades)
            return total_grade / len(self.grades)

    def __repr__(self):
        """Return name of the student."""
        return str(self.name)

    def add_grade(self, course: Course, grade: int):
        """Add grade to students grade list."""
        self.grades.append((course, grade))