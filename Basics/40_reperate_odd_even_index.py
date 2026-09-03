# . Write a Python program to take a string and separate characters present at even index positions and odd index positions.
text = input("Enter a string: ")
even_chars = text[::2]
odd_chars = text[1::2]
print("Characters at even index positions:", even_chars)
print("Characters at odd index positions:", odd_chars)