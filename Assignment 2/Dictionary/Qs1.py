# Convert two lists into a dictionary.


l1 = ["English", "Maths", "Physics", "Chemistry"]
l2 = [90, 94, 85, 89]
res = {}
for subject in l1:
	for marks in l2:
		res[subject] = marks
	l2.remove(marks)
print("Resultant dictionary is : " + str(res))