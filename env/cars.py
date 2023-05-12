# copying a List
my_foods = ['amala', 'rice', 'semo', 'tuwo', 'eba', 'ewedu']
friend_foods = my_foods[:]

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friends foods are:")
print(friend_foods)

# Defininig a tuple
# dimensions = (200, 50)
# Looping though tuple 
# for dimension in dimensions:
#  print(dimension)
# buffet
restaurant = ['rice', 'chicken', 'salad', 'ogufe', 'ewa', 'fish']
print("List of foods:")
for restaurant in restaurant:
    print(restaurant)