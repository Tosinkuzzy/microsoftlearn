# Checking for inequality
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("Hold the anchovies!")
 
# Checking whether a value in a list
requested_toppings = ['onions', 'mushrooms', 'pineapple']
'mushrooms' in requested_toppings
True
'pepperoni' in requested_toppings
False

favourite_toppings = input("Favourite Toppings Order:")
toppings = ['sugar', 'soda', 'cream']
print("Available == 'favourite_toppings'? I predict True")
print(toppings == 'favourite_toppings')

print("\Available == 'toppings'? I predict False")
print(toppings = 'toppings')