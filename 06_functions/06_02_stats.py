'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(example_list): #only one return statement per function!
  min = example_list[0]
  
  maxi = example_list[-1]
  
  sum = 0
  for i in example_list:
    sum += i
  
  average = sum / 7
  
  return min, maxi, average, sum

# call the function below here
print(stats(example_list)) #prints a tuple - is there a possibility to access f.e. the min only???

result = list(stats(example_list))

for i in range(0, len(result)):
  print(result[i])