'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

# Can be solved more elegantly via loops - but thats for later. Question is, 
if there is no more better way to use .count method to count vowels (did research it and tried it multiple times, but
coudlnt figure it out)#

'''
# Input sentence from user
# variables that contain vowels
# show results (total_count and individual count)

data = str(input("Pls enter your sentence: "))
sentence = data.lower()

a = sentence.count("a")
e = sentence.count("e")
i = sentence.count("i")
o = sentence.count("o")
u = sentence.count("u")

total_count = a + e + i + o + u
print(total_count)

print("a =", a)
print("e =", e)
print("i =", i)
print("o =", o)
print("u =", u)
