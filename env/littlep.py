# Build a sentence 
# Ask user for input
names = input("What is your name? ")
# Accessing Element in a List
print("Hi! " + names.title())
# Using individual Values from List
message = "Welcome to royal luxury Car!"
print(message)
# More sentence
# Sorting a List Permanently with the sort() Method
car = ['bmw', 'innoson', 'audi', 'toyota', 'subaru', 'tesla', 'toyota', 'honda', 'innoson']
# Changing element
car[1] = 'elegant'
car[3] = 'kia'
# Adding element
car.append('ford')
# Change the order of the list
car.sort()
print(car)
# Getting input from user
car = input("What car do you want? ")
# message 
message = "I would like to own a " + car.title() + "."
print(message)