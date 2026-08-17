import csv

total = 0
passing = 0
highest_score = -1
highest_name = ""
lowest_score = 101
lowest_name = ""

try: 
    with open("students.csv", "r", newline='') as read:
        csv_reader = csv.DictReader(read)
        students = []

        for row in csv_reader:
            try:
                score = int(row["Score"])
                total += score
                students.append({"Name": row["Name"], "Score": score})
            except ValueError:
                print(f"Invalid score: {row['Score']}, skipping")
                continue

            if (score >= 60):
                passing += 1

    total_student = len(students)
    average = round(total / total_student, 2)

    for student in students:
        if (student["Score"] > highest_score):
            highest_score = student["Score"]
            highest_name = student["Name"]
        if (student["Score"] < lowest_score):
            lowest_score = student["Score"]
            lowest_name = student["Name"]

    with open("report.txt", "w") as writer:
        writer.write(f"Average marks: {average}\n")
        writer.write(f"Highest mark: {highest_name}\n")
        writer.write(f"Lowest mark: {lowest_name}\n")
        writer.write(f"Total passing students: {passing}\n")

except FileNotFoundError:
    print("File not found.\n")

except ZeroDivisionError:
    print("No data saved in file.\n")

finally:
    print("Report generated.\n")
