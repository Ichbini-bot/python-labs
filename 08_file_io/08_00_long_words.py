'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
#list = []

with open("c:/Users/tobis/Documents/CodingNomads/labs/08_file_io/words.txt", "r") as list1:
    for word in list1.readlines():
        word = word.rstrip() #=> discuss: if i comment this out, then I get as well words with 20 chars!
        if len(word) > 20:
            print(word)
            #list.append(word)
           
#print(list)





