# Filling a Dictionary with User Input
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # prompt for the person's name and respnse.
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
if repeat == 'no':
    polling_active = False

    # Polling is complete. show the results.
    print("\n--- Poll Results ---")
for name, responses in response.items():
    print(name + " would like to climb " + response + ".")