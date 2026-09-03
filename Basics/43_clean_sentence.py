# 15. Take a sentence containing double spaces and unwanted spaces at the beginning or end. Clean the sentence.
sentence = input("Enter a sentence with extra spaces: ")
cleaned_sentence = sentence.strip().replace("  ", " ")
print("Cleaned sentence:", cleaned_sentence)