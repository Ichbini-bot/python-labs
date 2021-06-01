'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!

# first need to make tuples out of it
# Then need to sort it => check: https://github.com/CodingNomads/different-solutions


'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}

result_list = []

for key, value in input_dict.items():
      temp_list = key, value
      result_list.append(temp_list)
print(result_list) 

print(sorted(result_list, key=lambda value: value[1]))
