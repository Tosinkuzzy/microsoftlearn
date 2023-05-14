# if-elif-else chain
age = 19
if age < 20:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
# set the value of price
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age >= 65:
    price = 15
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
