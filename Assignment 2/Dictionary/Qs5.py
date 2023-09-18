#   Delete a list of keys from a dictionary.


Dict1 = { "Name": "Dipchandri", "Age":19, "City": "Kolkata" }

keys = ["Name", "Age"]

for k in keys:
    Dict1.pop(k)
print(Dict1)