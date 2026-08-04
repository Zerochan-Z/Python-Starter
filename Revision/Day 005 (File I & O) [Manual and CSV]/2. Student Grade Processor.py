filename = r"Revision\Day 005 (File I & O) [Manual and CSV]\grades.txt"
with open(filename, "w") as input:
    input.write("Alice, 85\n")
    input.write("Bob, 92\n")
    input.write("Charlie, 78\n")
    input.write("Diana, 95\n")
    input.write("Eve, 88\n")
    input.write("Frank, 73\n")
    input.write("Grace, 91\n")
    input.write("Henry, 67\n")
    input.write("Ivy, 82\n")
    input.write("Jack, 79")

with open(filename, "r") as read:
    grades = read.readlines()
    student_scores = {}
    for i in grades:
        sentence = i.strip()
        print(sentence)

        parts = i.split(", ")
        name = parts[0]
        marks = int(parts[1])

        student_scores[name] = marks

    print("Total students: ", len(student_scores))

    # Simpler way
    for name, score in student_scores.items():
        if (score == max(student_scores.values())):
            high_name = name
        if (score == min(student_scores.values())):
            low_name = name
    print("Highest score: ", high_name, "-",  max(student_scores.values()))
    print("Lowest score: ", low_name , "-", min(student_scores.values()))
    print("Average score: ", round(sum(student_scores.values())/ len(student_scores), 1))

    # More advanced
    print("Highest score person: ", max(student_scores, key = student_scores.get))
    # student_scores = collection to search through
    # key = student_scores.get = comparison value for each item
    # if only key = student_scores.get  ERROR
    # Because .get is a function, but max() require a iterable (list/tuple)

    """ 
    How key = student_scores.get works
    student_scores.get is a function that:
    Takes a key (a student name)
    Returns the value (their score)
    So max() does this:
    Look at the first key: "Alice"
    Call student_scores.get("Alice") → returns 85
    Look at the second key: "Bob"
    Call student_scores.get("Bob") → returns 92
    Compare 85, 92, 78, 95, etc.
    Find the largest score: 95
    Return the key that gave that score: "Diana"
    """