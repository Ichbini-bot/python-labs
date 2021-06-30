'''
filename = "c:/Users/tobis/Documents/CodingNomads/labs/08_file_io/words.txt"

def linecount(filename):
        count = 0
        for line in open(filename):
            count += 1
        return count

print(linecount(filename))
'''

list1 = ["ab", "abc", "abcd", "ba", "bac", "bacd", "bac"]

list2 = []

for word in range(len(list1)-1,-1,-1):
    print(list1[word+1])



'''
words = []

with open("c:/Users/tobis/Documents/CodingNomads/labs/08_file_io/words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

print(words)
'''



#with open("c:/Users/tobis/Documents/CodingNomads/labs/08_file_io/output.txt", "w") as fout:
#    fout.write("blabla blablab")