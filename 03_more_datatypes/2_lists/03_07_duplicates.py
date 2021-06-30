'''

Write a script that removes all duplicates from a list.

'''

from _typeshed import SupportsLessThan


list_ = [1, 2, 3, 4, 3, 4, 5]

print(list_)
list_no_dupes = set(list_)
print(list_no_dupes)
list_final = list(list_no_dupes)
print(list_final)





