# building a multi-line string
# the first line stores the first part of the message.
# second line operator += takes the string that was stored in prompt
# add the new string onto it
# the prompt now span two lines. 
prompt = "If you tell us who you are, we can personalise the messages you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print("\nHello, " + name.title() + "!")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")

# Letting the User Choose When to Quit
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' to end the program.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")