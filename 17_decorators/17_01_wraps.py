"""
Write a decorator function that wraps text passed to it in a html <p> tag.
"""

def decor_func(func):
  def wrapper_func(msg):
    return f"<p>{func(msg)}</p>"
  return wrapper_func

@decor_func
def test(var):
  return var

print(test("now with p tag"))

def p_decorate(func):
   def func_wrapper(name):
       return f"<p>{func(name)}</p>"
   return func_wrapper

@ p_decorate
def get_text(name):
   return f"lorem ipsum, {name} dolor sit amet"

print(get_text("John"))