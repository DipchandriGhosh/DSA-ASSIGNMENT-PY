# Add a list of elements to a set.

s = {"Yellow", "Orange", "Black"}
l = ["Blue", "Green", "Red"]

print(type(s))
print(type(l))

s.update(l)
print(s)

print(type(s))
