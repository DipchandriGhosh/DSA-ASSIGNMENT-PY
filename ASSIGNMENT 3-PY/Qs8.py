#Q8. Check for palindrome

def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")  # Remove spaces and punctuation, and convert to lowercase
    return s == s[::-1]

input_string = "A man, a plan, a canal, Panama!"
result = is_palindrome(input_string)
print(result)  # Output: True
