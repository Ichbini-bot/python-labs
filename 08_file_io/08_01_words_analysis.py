'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

#list1 = ["abcd", "ab", "abc", "abcd", "ba", "bac", "bacd", "bac"]

list1 = []

with open("c:/Users/tobis/Documents/CodingNomads/labs/08_file_io/words.txt", "r") as file:
    for word in file.readlines():
        word = word.rstrip()
        list1.append(word)


#shortest via function:
def shortest(list):
    p = 100
    s = []

    for item in list:
        if len(item) < p:
            s = [item]
            p = len(item)
        elif len(item) == p:
            s.append(item)
    return s

p = 100
s = []

for item in list1:
    if len(item) < p:
        s = [item]
        p = len(item)
    elif len(item) == p:
        s.append(item) #if not via .append: item gets overwritten! [ab] => [ba] instead of [ab, ba]!!!

#longest via function:
def longest(list):
    p = 0
    l = []

    for item in list:
        if len(item) > p:
            l = [item]
            p = len(item)
        elif len(item) == p:
            l.append(item)
    return l

p = 0
l = []

for item in list1:
    if len(item) > p:
        l = [item]
        p = len(item)
    elif len(item) == p:
        l.append(item)

print("shortest via function is: ", shortest(list1))

print("longest via function is: ", longest(list1))

filename = "c:/Users/tobis/Documents/CodingNomads/labs/08_file_io/words.txt"

def linecount(filename):
        count = 0
        for line in open(filename):
            count += 1
        return count

print(linecount(filename))