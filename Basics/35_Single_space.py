# Write a Python program to take a sentence, detect double spaces, and replace them with single spaces.
sentence = input("Enter a sentence: ")
print("Contains double spaces?", "  " in sentence)
print("Updated sentence:", sentence.replace("  ", " "))