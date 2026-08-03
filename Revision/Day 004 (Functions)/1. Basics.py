# Functions are automatically assigned
# float, void, string

def welcome_message(): 
    # void = return nothing
    print("Welcome to the Student Database!")

def average_score(scores): 
    # return float not double (dont have such data type)
    total = sum(scores)
    return round(total / len(scores), 2)

def add_student(database, name, score = 0): 
    # return data from dict
    database[name] = score
    return database

def add_grade_prefix(grades):
    # modifies the original list because lists are passed by reference    
    for i in range(len(grades)):
        grades[i] += 10

def min_max(numbers): 
    # (automatically assigns data type)
    # unlike C++ stricter format
    min = numbers[0]
    max = numbers[0]
    for i in range(len(numbers)):
        if (min > numbers[i]):
            min = numbers[i]
        if (max < numbers[i]):
            max = numbers[i]

    return min, max


students = ["Alice", "Bob", "Charlie"]
welcome_message()
print("Average score: ", average_score([85, 92, 78, 90]))
num_list = [10, 20, 30, 40]
add_grade_prefix(num_list) # added 10 for every [i]
print("After adding 10: ", num_list)

print(min_max(num_list))
print("Minimum value: ", min(num_list))
print("Maximum value: ", max(num_list))