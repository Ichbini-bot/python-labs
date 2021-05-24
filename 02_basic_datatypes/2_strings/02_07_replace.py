'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# Input sentence from user
# Input sign from user
# Store first letter
# Replace first letter with sign

sentence = input("Please enter your sentence: ")
sign = input("Please enter your sign: ")
first_letter = sentence[0]

# more directly / without use of additional variable:
print(sentence.replace(first_letter, sign))

# use of additional variable:
sentence_new = sentence.replace(first_letter, sign)
print(sentence_new) 
