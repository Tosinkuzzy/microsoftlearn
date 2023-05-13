# Checking wether a value is not in a list
# Taking user input
# if value of users not in list banned_list return True.
# execute the indented line.
# user='marie' 
# whether a user can edit profile.
# game_active = True
# can_edit = False
user = input("username:")
banned_user = ['andrew13', 'jacob10', 'james15', 'amo110s', 'alex331']
if user not in banned_user:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + " you are limited for comments")

