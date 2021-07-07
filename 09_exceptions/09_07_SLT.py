'''
class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("There was a problem")
except Exception as e:
    print(e)
'''
'''
list1 = ""

with open("09_exceptions/books/slt.txt", encoding="utf8") as file:
    for line in file:
        for word in line:
            list1 += word

print(list1)
list2 = list1[2]
print(list2)
'''

class Myexception(Exception):
    pass

list1 = ["lorem", "ipsum", "sit", "dolor", "prince", "lorem", "ipsum", "prince", "dolor", "ipsum"]


try:
    if "prince" in list1:
        raise Myexception
except Myexception:
    print("prince is in list")


'''
def check_for(list):
    prince_counter = 0
    for word in range(10):
        if list[word] == "prince":
            prince_counter += 1
    print(f"word prince occurs {prince_counter} times")


#check_for(list1)

'''
'''
five_words = []
with open("09_exceptions/slt.txt", "r") as file:
    for line in file:
        for word in line.split():
            five_words.append(word)

print(five_words)
print(five_words[0:10])

'''
'''

list1 = ["lorem", "ipsum", "sit", "dolor", "prince", "lorem", "ipsum", "prince", "dolor", "ipsum"]



for word in range(2):
    words = []
    words.append(list1[word])

print(words)
'''