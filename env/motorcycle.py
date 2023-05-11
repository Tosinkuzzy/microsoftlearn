# Modifying Element in a List
motocycles = []
# Appending values to element
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')

print(motocycles)
# Inserting Element in a List
motocycles.insert(4, 'ducati')
print(motocycles)
# Removing an item Using the del statment
del motocycles[0]
print(motocycles)
# Let pop a motocyles from the list of motocycles
popped_motocycles = motocycles.pop()
print(motocycles)
print(popped_motocycles)
# Print a statement
last_owned = motocycles.pop(1)
print("The motocycle I owned was a " + last_owned.title() + ".")
first_owned = motocycles.pop(0)
print('The first motocycle i owned was a ' + first_owned.title() + '.')
