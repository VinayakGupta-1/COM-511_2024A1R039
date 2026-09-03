# Write a Python program to take a word and count the number of vowels a, e, i, o, u.
word = input("Enter a word: ").lower()
count_a = word.count("a")
count_e = word.count("e")
count_i = word.count("i")
count_o = word.count("o")
count_u = word.count("u")
total_vowels = count_a + count_e + count_i + count_o + count_u

print(
    f"a: {count_a}, e: {count_e}, i: {count_i}, o: {count_o}, u: {count_u}"
)
print("Total vowels:", total_vowels)




