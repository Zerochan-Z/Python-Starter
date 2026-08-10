import csv

try: 
    with open("students.csv", "r", newline= '') as read:
        data_csv = csv.DictReader(read)
        totalMarks = 0
        passing_students = 0
        
        for row in data_csv:
            try:
                score = int(row['Score'])
            except ValueError:
                print(f"Invalid score: {row['Score']}, skipping.\n")
                continue

            if (score >= 60):
                totalMarks += score
                passing_students += 1

    average = totalMarks / passing_students
    
    with open("result.txt", "w") as write:
        write.write(f"Average Score: {average:.1f}")

except FileNotFoundError:
    print("The file is not found.\n")

except ZeroDivisionError:
    print("No passing students.\n")

finally:
    print("Calculation completed.\n")