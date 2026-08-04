filename = r"Revision\Day 005 (File I & O) [Manual and CSV]\students.txt"
file = open(filename, "w")
file.write("Alice, 85\n")
file.write("Bob, 92\n")
file.write("Charlie, 78\n")
file.close()

file = open(filename, "r")
text = file.read()
print(text)
file.close()

# Part 2: With statement 
# No need to close file
filename2 = r"Revision\Day 005 (File I & O) [Manual and CSV]\books.txt"
with open(filename2, "w") as books:
    books.write("Phigros, 29102\n") 

with open(filename2, "r") as books:
    text = books.read()
    print(text)

with open(filename2, "a") as adder:
    adder.write("How to use four fingers, 03133\n")

with open(filename2, "r") as reading:
    lines = reading.readlines()
    print(lines, "\n")

    for i in lines:
        sentence = i.strip()
        print(sentence)