#   Change value of a key in a nested dictionary

dict1 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

dict1['emp3']['salary'] = 8500
print(dict1)