# Student Data Manager

students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 78},
    {"name": "Charlie", "marks": 92},
    {"name": "David", "marks": 67},
    {"name": "Eva", "marks": 74}
]

# Calculate topper
topper = max(students, key=lambda x: x['marks'])
print(f"Topper: {topper['name']} with {topper['marks']} marks")

# Calculate class average
total_marks = sum(s['marks'] for s in students)
average = total_marks / len(students)
print(f"Class Average: {average:.2f}")

# Assign grades
def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

for s in students:
    grade = assign_grade(s['marks'])
    print(f"{s['name']} → Marks: {s['marks']}, Grade: {grade}")
