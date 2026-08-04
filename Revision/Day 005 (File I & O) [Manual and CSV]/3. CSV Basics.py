import csv

file = r"Revision\Day 005 (File I & O) [Manual and CSV]\grades.csv"
with open(file, "w") as write:
    csv_writer = csv.writer(write)
    csv_writer.writerow(["Alice", 85]) # Creates blank line after it
    csv_writer.writerow(["Bob", 92])
    csv_writer.writerow(["Charlie", 78])

with open(file, "r") as read:
    csv_reader = csv.reader(read)
    for row in csv_reader:
        if row: # if row != NULL then print row
            print(row)
