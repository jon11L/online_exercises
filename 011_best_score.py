# Problem : Write a python program that takes a list of tuples (each tuple containing a name and score)
# and return the name of the person with the highest score

name_list = []
name_list.append(('louise', 40))
name_list.append(('Paul', 15))
name_list.append(('Agatha', 55))
name_list.append(('Duck', 37))

name_list = sorted(name_list, key= lambda x: x[1], reverse=False)

for i, name in enumerate(name_list, start=1):
    print(f"{i} - {name[0]} {name[1]}")