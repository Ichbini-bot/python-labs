'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
fish_list = []

for word in fish_tuple:
    if "fish" in word:
        fish_list.append(word)

print(fish_list)

print("VIA LIST COMPREHENSION")

def go_fish(tuple):
    fsh_list = [word for word in tuple if "fish" in word]
    return fsh_list

print(go_fish(fish_tuple))