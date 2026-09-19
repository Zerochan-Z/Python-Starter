import csv

file = r"Revision\Day 006 (Exception Handling)\students.csv"
count = 0

try:
    with open(file, "r") as read:
        csv_reader = csv.reader(read)

        for row in csv_reader:
            if row: 
                count+= 1
                print(row)

        print(f"Total students: {count}")

except FileNotFoundError:
    print("No file is detected.")
