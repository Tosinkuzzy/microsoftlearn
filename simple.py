name = input("What is your name? ")
print(f"Welcome, {name}!")
gender = input(f"Male or female? ")
sport = input(f"Do you love sport? ")
birth_age = input("How old are you? ")
birth_age = int(birth_age)
a = 18
b = 100
if a <= b:
    print(f"You are {2023 - birth_age} years old")
elif a == b:
    print("{2023 - birth_age}")
else:
    print("Sorry you are not allowed! {2023 - birth_age}")
