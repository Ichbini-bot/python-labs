'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

#print(famous_quotes[0]["full_name"])



for entry in famous_quotes:
    if entry['full_name']:                          # ?????????????????????new to me to access a dict like that....????
        first_last = entry['full_name'].split()
        last_name = first_last[-1]
        first_name = " ".join(first_last[0:len(first_last)-1])               # doesnt work for Edsger W. Dijkstra...
    print(f"{entry['quote']} - {last_name}, {first_name}")

#print(f"{item['quote']} - {item['full_name']}")
      
