'''

nums = [3, 8, 1, 6, 10, 4]
filtered_num = []

for i in nums:
    if i > 5:
        filtered_num.append(i * 2)

print(filtered_num)
'''

# _Conditional expression_

nums = [3, 8, 1, 6, 10, 4]
filtered_num = [i * 2 for i in nums if i > 5]
print(filtered_num)