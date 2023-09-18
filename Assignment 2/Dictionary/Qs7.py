#   Rename key of a dictionary.

Dict1 = { "Name": "Dipchandri", "Age":19, "City": "Kolkata" }
Dict1['location'] = Dict1.pop('City')
print(Dict1)