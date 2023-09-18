#   Initialize dictionary with default value.

student = ["Dipchandri", "Arpan"]
defaults = {"Designation": "Student", "Department": "BTech"}
 
result = dict.fromkeys(student, defaults)
print(result)
 
# Individual data
print("\nDipchandri :",result["Dipchandri"])
print("\nArpan :",result["Arpan"])