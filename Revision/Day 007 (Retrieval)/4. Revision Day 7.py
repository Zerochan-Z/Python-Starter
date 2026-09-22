numbers = [4, 2, 7, 1, 9]

print(sorted(numbers))
even_num = [x for x in numbers if x % 2 == 0]
print(even_num)

average = sum(even_num) / len(even_num)
print(average)
