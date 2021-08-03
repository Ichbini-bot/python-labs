'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''
def decor_func(func):
  def wrapper_func(msg, tag):
    return f"<{tag}>{func(msg)}</{tag}>"
  return wrapper_func

@decor_func
def test(var):
  return var

print(test("first tag", "H1"))
print(test("now with a different tag", "div"))
print(test("finally with a last new tag", "body"))


'''
inp = input("pls enter sentence ")
tag = input("pls enter HTML tag ")

def html_tag(inp, tag):
    return f"<{tag}>{inp}</{tag}>"

print(html_tag(inp, tag))
'''
