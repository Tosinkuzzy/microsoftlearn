# Build a sentence 
# Ask user for input
names = input("What is your name? ")
# Accessing Element in a List
print("Hi! " + names.title())
# Using individual Values from List
message = "Welcome to Innoson Vehicles!"
print(message)
# More sentence
# print("Top Cars" + "\n")
# Sorting a List Permanently with the sort() Method
car = ['fox', 'umu', 'carrier', 'ivm carrier', 'g4', 'g6', 'g40', 'ivm carrier 4x4 pickup']
print("List of Cars:")
# Looping through a slice 
# for car in car[:10]:
for car in car:
    print(car.title())
# Changing element'
# Adding element
# car.append('g7')
# Change the order of the list
# car.sort()
# Reverse order
# car.sort(reverse=True)
print(car)
# Getting input from user
car = input("Your Order? ")
# message 
message = "I would like to own a " + car.title() + "."
print(message)
# Defining car func, passing parameter color
# User input
# for loop using, slice
def car_color(color):
    print("Car Color List:")
    color = ['red', 'yellow', 'white', 'black']
    color = input("Pick color: ")
    if color:
       # print(color.title())
     print("I would like to own a " + color.title() + " " + car.title() + ".")
    #print(color)
    messages = "Request Accepted."
    print(messages)
       # print(color.title())
      # print(color)
    # color = input("Pick car color: ")
    # if color in color:
# print("I would like to own a " + color.title() + " " + car.title() + ".")
# callable func
car_color("[]")
# car price using if-elif-else chain
def budget(car_budget):
    car_budget = 30000 #input(str("Budget:"))
    if car_budget < 20000:
        price = 22450
    elif car_budget > 100000:
        price = 105656
    else:
        price = 170000
print("Your preferred car price is $" + str(car_budget) + ".")