#   Create a dictionary by extracting the keys from a given dictionary.

Dict1 = { "Name": "Dipchandri", "Age":19, "City": "Kolkata" }

keys = ["Name", "Age"]

Dict2 = {k: Dict1[k] for k in keys}
print(Dict2)