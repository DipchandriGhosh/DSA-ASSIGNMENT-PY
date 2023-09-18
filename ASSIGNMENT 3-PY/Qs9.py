#Q9. Abbreviation in python

def get_abbreviation(word):
    words = word.split()  # Split the word into individual words if it contains spaces
    abbreviation = ''.join(word[0].upper() for word in words)  # Take the first letter of each word and convert to uppercase
    return abbreviation

input_word = "central processing unit"
abbreviation = get_abbreviation(input_word)
print("Abbreviation:", abbreviation)  # Output: CPU
