#   Remove empty strings from the list of strings.

list=["", "My", "", "name", "", "is", "", "Dipchandri", ""]
print("Original list : ", list)
while("" in list):
    list.remove("")
print("Modified list : ", list)