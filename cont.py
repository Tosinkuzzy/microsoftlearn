from datetime import date
print(date.today())
parsecs = 11
lightyears = parsecs * 3.26
parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")