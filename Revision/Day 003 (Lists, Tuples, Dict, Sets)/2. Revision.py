students = ["Alice", "Bob", "Charlie"]

print(students)
print(students[1])
students.append("Diana")
print("Updated lists: ", students)

course_grades = (85, 92, 78, 90)
print(course_grades)
print(course_grades[2])

"""
course_grades[0] = 100
    course_grades[0] = 100
    ~~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""

unique_courses = {"Math", "Physics", "Math", "Chemistry", "Physics"}
print("After filtered repeated: ", unique_courses)
unique_courses.add("Biology")
print("After adding biology: ", unique_courses)

student_scores = {
    "Alice" : 85,
    "Bob": 92,
    "Charlie": 78
}

print(student_scores)
print(student_scores["Bob"])
student_scores.update({"Diana": 95})
print(student_scores)


# 1. What happens if you try to add "Math" to the set again?
#    Run it and see. Why does this happen?
#   Ans: Nothing, sets ignore duplicates.


# 2. What's the difference between:
#    my_list = [1, 2, 3] Can be change
#    my_tuple = (1, 2, 3) Cannot change
#    my_dict = {1: "one", 2: "two", 3: "three"} key-value pair, modify/get by key
#   Ans: 

# 3. In C++, which bracket would you use for an array? []
#    In C++, which bracket would you use for a vector? []
#    In Python, which bracket do you use for a list? []