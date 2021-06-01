'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

input from user: 10 numbers
store in list
print second list: 4th, 6th, 8th, 10th
third list: 9th, 7th, 5th, 3rd, 1st
'''
# empty list
list = []
# user input
for i in range(1, 11):
    data = int(input("pls enter number: "))
    list.append(data)
    
print(list)

# get 2n, 4th, 6th etc number
list_uneven = list[1: :2]
print(list_uneven)
# get 9th, 7th etc. number
list_even = list[-2: : -2]
print(list_even)
# concatenate lists into one final list
final_list = list_uneven + list_even
print(final_list)



