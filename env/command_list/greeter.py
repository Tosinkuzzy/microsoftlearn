def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ",")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

    describe_pet('hamster', 'harry')
    describe_pet('dog', 'willie')

def describe_city(city_name, state_name):

    """Display city and state."""
    print(city_name + "is in " + ",")
    print(state_name.title() + "\nstate")

    describe_city('owo', 'ondo')
    describe_city('akure', 'ondo')

musician = get_formatted_name('alex', 'greg', 'hend')
print(musician)

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendix', age=27)
print(musician)
