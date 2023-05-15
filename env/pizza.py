# Store information about a pizza being ordered.
# Dictionary that holds information about a pizza 
# that has been ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t + topping")