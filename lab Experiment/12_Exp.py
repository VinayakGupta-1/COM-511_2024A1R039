# Create a function max of three that takes three numbers as arguments and returns the largest of them and 
# also create a parameter function that checks whether a given number is Armstrong or not.

def max_of_three(a, b, c):
    return max(a, b, c)


def armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number:", max_of_three(a, b, c))

n = int(input("Enter a number: "))

if armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")