# Checking if user input is even or odd
name = input("Enter a number, and i'll tell you if it's even or odd: ")
number = int(name)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
     print("\nThe number " + str(number) + " is odd.")