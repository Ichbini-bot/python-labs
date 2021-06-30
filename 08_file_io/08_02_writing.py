'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

list1 = ["ab", "abc", "abcd", "ba", "bac", "bacd", "bac"]

reverse_list = []

for i in range(len(list1)-1,-1, -1):
    reverse_list.append(list1[i])

print(reverse_list)