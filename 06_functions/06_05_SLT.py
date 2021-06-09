'''
mockup_input = input("pls enter sentence: ")


def titlecase(text):
    titlecase = []
    for word in text.split():
        cap_word = word.capitalize()
        titlecase.append(cap_word)
    return " ".join(titlecase)

print(titlecase(mockup_input))
'''
'''
name = "Mycroft"

def print_name_box():
  print(name)

  def smaller_box():
    
    (re)assigning a variable within the same scope
    overwrites the same variable from an outer scope
    -> you cannot use it *before* assigning it,
    if you assign it at all anywhere in that scope.
    --TASK--: uncomment the below print() statement
        and interpret the results when running it


    #print(name)
    name = "Sherlock"

    def smallest_box():
      
      inner scopes always draw from the next-outer layer
      after 'name' got overwritten, the name that will
      be printed is NOT the global-scope name anymore
      

      print(name)

    smallest_box()

  smaller_box()

print_name_box()
'''
'''
def shout(name):
    loud_name = name.upper()
    return loud_name

print(shout("wilma"))

def sqr(n) -> int:
    return n * n
print(sqr(4))
'''

l = [1,2,3]

print(l)
first = l[0]
print(first)
l.remove(l[0])
print(l)
l.append(first)
print(l)

