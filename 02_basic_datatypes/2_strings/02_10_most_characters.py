'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
# Get user input
# check each input for length and store info
# print
# challenge: compare lengths and only print "longest" one

first = str(input("Pls enter a word or sentence: "))
second = str(input("Pls enter a word or sentence: "))
third = str(input("Pls enter a word or sentence: "))

first_len, second_len, third_len = len(first), len(second), len(third)

# Cant get rid of the indent before the comma... (4 , "len" vs. 4, "len")

print(first_len, ",", first)
print(second_len, ",", second)
print(third_len, ",", third)

# no clear result if words have same num count (prints the firs one)
if first_len >= second_len:
    print(first_len,",", first)
elif second_len >= third_len:
    print(second_len, ",", second)
else:
    print(third_len, ",", third)
