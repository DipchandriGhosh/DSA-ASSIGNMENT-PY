# Remove items from set1 that are not common to both set1 and set2.

s1={1,2,3,4}
s2={2,4,6,8}
s1.intersection_update(s2)
print(s1)