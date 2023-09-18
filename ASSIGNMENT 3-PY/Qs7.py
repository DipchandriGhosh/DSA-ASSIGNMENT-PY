#Q7. Reverse a string in python

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: "!dlroW ,olleH"