#  Write a Python program to take a word and print it in reverse order using slicing. Also check whether it is the same forward and backward.
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed:", reversed_word)
print("Is palindrome?", word == reversed_word)
