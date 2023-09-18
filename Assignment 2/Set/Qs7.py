# Check if two sets have any elements in common. If yes, display the common elements.

s1={1,2,3,4}
s2={2,4,6,8}

if s1.isdisjoint(s2):
    print("There are no common elements")
else:
    print("Common elements are:",s1.intersection(s2))