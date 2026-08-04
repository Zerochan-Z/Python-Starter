import csv
file = r"Revision\Day 005 (File I & O) [Manual and CSV]\grades.csv"

with open(file, "w", newline='') as write:
    csv_writer = csv.writer(write)
    # Wrong
    # csv_writer.writerow("Name, Score")
    # N,a,m,e,",", ,S,c,o,r,e
    csv_writer.writerow(["Name", "Score"])
    csv_writer.writerow(["Alice", 85])
    csv_writer.writerow(["Bob", 92])
    csv_writer.writerow(["Charlie", 78])

with open(file, "r", newline='') as read:
    csv_reader = csv.DictReader(read)
    student_grades = {}
    for row in csv_reader:
        name = row["Name"]
        score = row["Score"]
        student_grades[name] = int(score)
        print(name, score)

    total_students = len(student_grades)
    max_mark = max(student_grades.values())
    low_mark = min(student_grades.values())
    average = round(sum(student_grades.values()) / total_students, 1)

    print("Total students: ", total_students)
    print("Highest mark: ", max_mark)
    print("Lowest mark: ", low_mark)
    print("Average: ", average)
