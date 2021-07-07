'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable


2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

logic for challenge in 0907 SLT 

'''
'''
#Excercise 1:
list1 = []

with open("09_exceptions/books/war_and_peace.txt", encoding="utf8") as file:
    for line in file:
        for word in line.split():
            list1.append(word)

#print(list1)

#Exercise 2:
with open("09_exceptions/books/crime_and_punishment.txt", "w") as file:
    file.writelines("")

#Exercise 3:
import os

raw_files = os.listdir("09_exceptions/books")

for file in raw_files:
    try:
        with open(f"09_exceptions/books/{file}", "r", encoding="utf8") as f:
            first_line = f.readline()
            print(first_line[0])
    except IndexError as ie:
        print(f"file contains empty string - {ie}")

print("***'LINEAR'***")

try:
    with open("09_exceptions/books/war_and_peace.txt", encoding="utf8") as file:
        first_line = file.readline()
        print(first_line[0])
    with open("09_exceptions/books/crime_and_punishment.txt", encoding="utf8") as file:
        first_line = file.readline()
        print(first_line[0])
except IndexError as ie:
    print(f"file contains empty string {ie}")   
finally:
    with open("09_exceptions/books/pride_and_prejudice.txt", encoding="utf8") as file:
            first_line = file.readline()
            print(first_line[0])
'''

# Challenge:
import os

class MyCustomError(Exception):
    pass

raw_files = os.listdir("09_exceptions/books")

for file in raw_files:
    try:
        list = []
        with open(f"09_exceptions/books/{file}", "r", encoding="utf8") as f:
            for line in f:
                for word in line.split():
                    list.append(word)
        first_hundret = list[0:100]
        print(first_hundret)
        if "Prince," in first_hundret:
            raise MyCustomError
    except IndexError as ie:
        print(f"file contains empty string {ie}")   
    except MyCustomError:
        print("file contains the word prince in the first 100 words")

