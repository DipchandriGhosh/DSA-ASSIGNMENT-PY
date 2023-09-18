#Q10. Write a program to implement searching and sorting in a list of words.

def linear_search(words, target):
    for i, word in enumerate(words):
        if word == target:
            return i
    return -1

def main():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    print("Original List:", words)

    target = "fig"
    linear_index = linear_search(words, target)
    print(f"Linear Search: '{target}' found at index {linear_index}")

if __name__ == "__main__":
    main()