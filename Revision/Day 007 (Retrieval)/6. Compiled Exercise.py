nums = [1, 2, 3, 4, 5, 6]

even_num = [x for x in nums if x % 2 == 0]
print(even_num)

person = {"Name: " : "Tom", "Age : ": 20}

for key, value in person.items():
    print(key, value)

print(person.keys(), ": ", person.values())

def add(a, b):
    return sum([a, b])

print(add(3,5))

with open(r"test.txt", "r") as read:
    sentence = read.read()
