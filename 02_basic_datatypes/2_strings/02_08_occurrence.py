'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
# Input sentence from user
# Input letter from user
# Find index of letter in sentence
# Print result

sentence = input("Pls enter a sentence: ")
letter = input("Pls enter a letter: ")

# Indirectly (via additional variable):
index = sentence.find(letter)
print(index)

# Directly (no additional variable needed):
print(sentence.find(letter))