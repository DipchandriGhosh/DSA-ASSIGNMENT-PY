#   Concatenate two lists index-wise.

list1=["Myse", "Dip"]
list2=["lf", "chandri"]
list3=[]
print("list1= ",list1)
print("list2= ",list2)
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print("After concatenating = ",list3)