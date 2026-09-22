text = "hello world hello"

words = text.split()

# Set empty dict
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
print(max(word_count, key=word_count.get))