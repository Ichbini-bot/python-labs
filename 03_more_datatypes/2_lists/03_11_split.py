'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

data = str(input("pls enter a sentence: "))

data = data.split()
print(data)

counter = 0
num = None

for i in data:
    curr_frequency = data.count(i)
    if curr_frequency > counter:
        counter = curr_frequency
        num = i

print(num)

'''
word_count = []
 
for word in data:
    counter = data.count(word)
    word_count.append(counter)

max_word = max(word_count)

print(max)

print(word_count)
print(max(word_count))
'''






