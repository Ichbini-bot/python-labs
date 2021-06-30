class Partner:
    database = [] # How can I visualize this? [["Maria", 21, False], ["Florian", 116, False]...] ]? or dictionary = [[name : "Maria", age : 21, likes_me : ]...
    def __init__(self, name, age, likes_me):
        self.database.append(self)
        self.name = name
        self.age = age
        self.likes_me = likes_me

Maria = Partner("Maria", 21, False)
Florian = Partner("Florian", 116, False)
Eve = Partner("Eve", 22, True)
Fiona = Partner("Fiona", 55, True)

#print(Partner(Maria.database))

for partner in Partner.database:
    if partner.age < 25 and partner.likes_me == True:
        print(partner.name +"(age " + str(partner.age) + ") likes you!") # => this would actually speak for dictionary
