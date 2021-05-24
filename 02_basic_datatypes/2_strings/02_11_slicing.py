'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
# User input name
# store first letter in variable
# store rest of name in variable
# combine through print function

name = str(input("Pls enter your first name: "))
letter = name[0].lower() + "ay"
rest_name = name[1:]

print(rest_name + letter)
