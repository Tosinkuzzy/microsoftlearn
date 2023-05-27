# Store information about a pizza being ordered.
# Dictionary that holds information about a pizza 
# that has been ordered.
# pizza = {
  #  'crust': 'thick',
   # 'toppings': ['mushrooms', 'extra cheese'],
#}
# Summarize the order.
#print("You ordered a " + pizza['crust'] + "-crust pizza " + 
 #     "with the following toppings:")

#for topping in pizza['toppings']:
 #   print("\t + topping")

# Arbitrary Number of Arguments
# Pizza sizes
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)