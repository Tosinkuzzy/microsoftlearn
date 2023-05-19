# Removing All instances of specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'dog' in pets:
    pets.remove('dog')

print(pets)
