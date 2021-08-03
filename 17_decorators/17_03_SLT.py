'''
def say_hi():
    print("Hi.")

hi = say_hi
hi()

def say_moo():
    print("moooooooo!")

list_ = [say_hi(), say_moo()]
list2 = [say_hi, say_moo]

print(list_)
print(list2[0]())
print(list2[1]())
'''
'''
def outer_func():
    msg = "Weeeeeekend!"
    def inner_func():
        print(msg)
    return inner_func

say_wee = outer_func()

say_wee()
'''
'''
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

say_wee = outer_func("du dödel")
say_wee()
say_wee = outer_func("du hirsch")
say_wee()
'''
'''
def decorator_func(initial_func):
    def wrapper_func(msg):
        print("wrapper function picked some...")
        return initial_func(msg)
    return wrapper_func

@decorator_func
def prettify(msg):
    print(msg)

prettify("flowers for you")
'''
'''
def decor_func(func):
  def wrapper_func(*args):
    print("="*30)
    pstr = func(*args)
    print("="*30)
  return wrapper_func

@decor_func
def greeting(name, name2):
  print(f"Hey {name} {name2}! Good morning")

greeting("Tobias", "Sebastian")
'''
'''
def outer_function():
  msg = "hello world"
  def inner_function():
    print(msg)
  return inner_function

outer_function()()
'''

def outer_func():
    msg = "Do you understand my scope??"
    def inner_func():
        print(msg)
    return inner_func

outer_func()()

def sum(a, b):
    print(a * b)

hi = sum
hi(10, 10)

def say_hi():
    print("Hi.")

def say_moo():
    print("moooooooo!")

list_ = [say_hi, say_moo()]
print(list_)

def my_func(msg):
    def inner_func():
        print(msg)
    return inner_func

message = "Now we have an argument!"
woohoo = my_func(message)
woohoo()

def decorator_func(initial_func):
    def wrapper_func():
        print("wrapper function picked some...")
        return initial_func()
    return wrapper_func

@decorator_func
def dec():
  return  "inside dec"

print(dec())