#   Remove all occurrences of a specific item from a list.

list = [5, 20, 15, 20, 25, 50, 20]

while 20 in list:
    list.remove(20)
print(list)