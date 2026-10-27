# Student Performance Analyzer

# Fixed grade categories
grade_categories = ("Excellent", "Good", "Pass", "Fail")


# Function to calculate average score
def calculate_average(scores):
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


# Function to classify grade
def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


# Function to count passing students
def count_passed(students):
    count = 0

    for student in students:
        if student["score"] >= 40:
            count += 1

    return count


# Student records
students = [
    {"name": "Aung Aung", "age": 21, "study_hours": 4.5, "score": 85},
    {"name": "Su Su", "age": 20, "study_hours": 3.0, "score": 65},
    {"name": "Mg Mg", "age": 22, "study_hours": 2.0, "score": 35},
    {"name": "Kyaw Kyaw", "age": 21, "study_hours": 5.0, "score": 90},
    {"name": "Hla Hla", "age": 19, "study_hours": 3.5, "score": 75}
]


# Validate scores
for student in students:
    if student["score"] < 0 or student["score"] > 100:
        print("Invalid score for", student["name"])
        raise ValueError("Score must be between 0 and 100")


# Display student performance report
print("===== STUDENT PERFORMANCE REPORT =====\n")

for student in students:
    grade = classify_grade(student["score"])

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Study Hours:", student["study_hours"])
    print("Score:", student["score"])
    print("Grade:", grade)
    print()


# Calculate summary statistics
scores = []

for student in students:
    scores.append(student["score"])

average_score = calculate_average(scores)
passed_students = count_passed(students)
failed_students = len(students) - passed_students
highest_score = max(scores)
lowest_score = min(scores)

top_student = max(students, key=lambda student: student["score"])


# Display summary report
print("===== SUMMARY =====")
print("Total Students:", len(students))
print("Average Score:", round(average_score, 2))
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Top Student:", top_student["name"])
print("Grade Categories:", grade_categories)