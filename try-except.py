# exception : events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(fraction)