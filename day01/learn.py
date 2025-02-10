a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

# Check if all numbers are equal
if a == b == c:
    print("All numbers are equal:", a)
else:
    largest = max(a, b, c)
    print("The largest number is:", largest)

    smallest = min(a, b, c)
    print("The smallest number is:", smallest)
