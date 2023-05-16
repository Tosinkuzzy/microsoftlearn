# A Dictionary in a Dictionary
# Define a dictionary called users with two keys

users = {
    'tosinkuzzy': {
        'first': 'tosin',
        'last': 'kuzzy',
        'location': "princeton",
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    'mcattie': {
        'first': 'mia',
        'last': 'khalifa',
        'location': 'california',
    }
}
# Loop through the user in Dictionary
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tfull name: " + full_name.title())
    print("\tlocation: " + location.title())