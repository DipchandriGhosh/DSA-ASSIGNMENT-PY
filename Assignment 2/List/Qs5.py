#   Iterate both lists simultaneously.

import itertools

subject=["Maths", "English", "Physics", "Chemistry"]
marks=[90, 95, 87, 82]
for (a, b) in zip(subject, marks):
    print(a, b)