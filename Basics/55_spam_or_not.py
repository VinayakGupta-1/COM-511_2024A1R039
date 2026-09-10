"""
Write a Python program to detect whether a comment is spam or not.
A comment should be treated as spam if it contains any of these
keywords:"make a lot of money", "buy now", "subscribe this", or "click this".
 """

comment = input("Enter your comment: ").lower()

if ("make a lot of money" in comment or
    "buy now" in comment or
    "subscribe this" in comment or
    "click this" in comment):

    print("This comment is spam.")
else:
        print("This comment is not spam.")