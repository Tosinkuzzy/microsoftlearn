# Checking wether a value is not in a list
user = input("username:")
banned_user = ['andrew13', 'jacob10', 'james15', 'amo110s', 'alex331']
if user not in banned_user:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + " you are limited for comments")

