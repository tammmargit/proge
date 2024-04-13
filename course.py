"""
Module-level docstring.

This module contains the definition of the Course class. which represents a course in a
school.
"""


class Course:
    """Course class."""

    def __init__(self, name: str):
        """Initialize a new course with the given name."""
        self.name = name
        self.grades = []

    def get_grades(self):
        """Return the list of grades for this course."""
        return self.grades

    def add_grade(self, student, grade):
        """Add a grade for a student to this course."""
        self.grades.append((student, grade))

    def get_average_grade(self):
        """Get the average grade for this course."""
        if len(self.grades) == 0:
            return -1
        else:
            total_grade = sum(grade for _, grade in self.grades)
            return total_grade / len(self.grades)

    def __repr__(self):
        """Return a string representation of the course."""
        return str(self.name)