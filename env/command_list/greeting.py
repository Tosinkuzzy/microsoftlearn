def greet_users(names):
    """Print a greeting message to each user in the List"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'alex', 'zara']
greet_users(usernames)