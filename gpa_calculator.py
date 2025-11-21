"""
GPA Calculator for CPSC Help Desk
- Matches your Trello checklist
- Includes unit tests at the bottom
"""

import unittest

# -----------------------------
# Grade → Quality Points Scale
# -----------------------------
GRADE_SCALE = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0,
}


def convert_grade_to_points(grade: str):
    """Convert a letter grade to quality points based on XULA-style scale."""
    if grade is None:
        return None
    grade = grade.upper().strip()
    return GRADE_SCALE.get(grade)


def calculate_gpa(grades, credit_hours):
    """
    Calculate GPA using quality points and credit hours.

    grades: list of letter grades e.g. ["A", "B", "C"]
    credit_hours: list of numbers e.g. [3, 3, 4]

    Returns: GPA rounded to 2 decimal places.

    Raises:
        ValueError if:
        - invalid grade
        - missing/invalid credit hours
        - total hours is zero
    """
    if len(grades) != len(credit_hours):
        raise ValueError("Grades and credit hours lists must be the same length.")

    total_quality_points = 0.0
    total_hours = 0.0

    for grade, hours in zip(grades, credit_hours):
        # Check for invalid or missing grade
        points = convert_grade_to_points(grade)
        if points is None:
            raise ValueError(f"Invalid grade entered: {grade}")

        # Check for invalid or missing credit hours
        if hours is None or hours <= 0:
            raise ValueError("Missing or invalid credit hours.")

        total_quality_points += points * hours
        total_hours += hours

    if total_hours == 0:
        raise ValueError("Total credit hours cannot be zero.")

    gpa = total_quality_points / total_hours
    return round(gpa, 2)


def run_gpa_calculator():
    """Simple CLI-based GPA calculator to match your user story."""
    print("\n--- GPA Calculator ---\n")
    print("Enter your courses one by one.")
    print("Type 'done' when you are finished.\n")

    grades = []
    credit_hours = []

    while True:
        grade = input("Enter a grade (A–F) or 'done' to calculate: ").strip()
        if grade.lower() == "done":
            break

        # Validate grade first
        if convert_grade_to_points(grade) is None:
            print(" Invalid grade entered. Try again with A, B, C, D, or F.\n")
            continue

        # Ask for credit hours
        hours_input = input("Enter credit hours for this course: ").strip()
        try:
            hours = float(hours_input)
            if hours <= 0:
                print(" Credit hours must be greater than 0.\n")
                continue
        except ValueError:
            print(" Invalid credit hours. Must be a number.\n")
            continue

        grades.append(grade)
        credit_hours.append(hours)
        print("✓ Course added.\n")

    if not grades:
        print("No courses entered. GPA cannot be calculated.")
        return

    # Try to calculate and handle any errors from calculate_gpa
    try:
        gpa = calculate_gpa(grades, credit_hours)
        print(f"\n🎓 Your GPA is: {gpa}\n")
    except ValueError as e:
        print(f" Error calculating GPA: {e}")


# -----------------------------
# Unit Tests
# -----------------------------

class TestGpaCalculator(unittest.TestCase):
    """Unit tests that match your acceptance criteria."""

    def test_single_course_gpa(self):
        """A single A in a 3-credit course should give 4.00 GPA."""
        gpa = calculate_gpa(["A"], [3])
        self.assertAlmostEqual(gpa, 4.00, places=2)

    def test_multiple_courses_gpa(self):
        """A mix of A and B should give the correct weighted GPA."""
        # A (4.0) in 3 hours, B (3.0) in 3 hours
        # (4*3 + 3*3) / (3+3) = 21/6 = 3.5
        gpa = calculate_gpa(["A", "B"], [3, 3])
        self.assertAlmostEqual(gpa, 3.50, places=2)

    def test_invalid_grade_raises(self):
        """Entering an invalid grade like 'Z' should raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_gpa(["Z"], [3])

    def test_missing_credit_hours_raises(self):
        """0 or negative credit hours should raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_gpa(["A"], [0])

        with self.assertRaises(ValueError):
            calculate_gpa(["A"], [-3])

    def test_zero_total_hours_raises(self):
        """Total hours of 0 is not allowed."""
        with self.assertRaises(ValueError):
            calculate_gpa([], [])

    def test_mismatched_list_lengths_raises(self):
        """grades and credit_hours must be same length."""
        with self.assertRaises(ValueError):
            calculate_gpa(["A", "B"], [3])  # 2 grades, 1 hour value


if __name__ == "__main__":
    run_gpa_calculator()
