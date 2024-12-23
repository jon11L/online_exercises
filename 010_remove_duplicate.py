# problem : Write a program that removes all duplicates from a list provided by the user, then sort the remaining elements in ascending order. Diff. Medium

import math

user_list = ["score", "boat", "music", "skate", "music", "water", "boat", "score" , "element", "boat", "music", "water", "boat", "score"]


# sort with a list
sorted_list = []
for i in user_list:
    if i not in sorted_list:
        sorted_list.append(i)

sorted_list.sort()
print(f"{sorted_list}\n")


# OR with a set to ensure no duplicates.
new_stored_list = set()
for i in user_list:
    new_stored_list.add(i)

sorted_set = sorted(new_stored_list)
print(sorted_set)