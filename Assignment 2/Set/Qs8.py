# Update set1 by adding items from set2, except common items.

s1={1,2,3,4}
s2={2,4,6,8}
s1.symmetric_difference_update(s2)
print(s1)