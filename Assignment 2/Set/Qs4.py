# Update the first set with items that don’t exist in the second set.

s1=set([1,2,3,4])
s2=set([2,4,6,8])
s1.difference_update(s2)
print(s1)