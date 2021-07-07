'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
try:
    with open("09_exceptions/integers.txt", "r") as num:
        number = num.readline()
        result = number + 5
        print(result)
except ValueError:
    print("Must be number - not string")
except IOError:
    print("IO Error - pls handle differently")
    
