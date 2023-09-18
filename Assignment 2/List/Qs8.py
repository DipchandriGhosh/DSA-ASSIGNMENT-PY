#   Extend nested list by adding the sublist.

l1=['a',['b','c'],'d']
l2=[1,2,3]
l1[1].extend(l2)
print(l1)