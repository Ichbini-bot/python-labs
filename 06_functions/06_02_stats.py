'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(example_list): #only one return statement per function?
  minimum = min(example_list)
  
  maxi = max(example_list)
  
  summary = sum(example_list)
  '''
  sum = 0
  for i in example_list:
    sum += i
  '''
  
  average = summary / len(example_list)
  
  return minimum, maxi, average, summary #returns a tuple

# call the function below here
minimum, maximum, average, summmary = stats(example_list)

print(minimum)
print(maximum)
print(average)
print(summmary)

#print(stats(example_list)) #prints a tuple - is there a possibility to access f.e. the min only???

'''
result = list(stats(example_list))

for i in range(0, len(result)):
  print(result[i])
'''