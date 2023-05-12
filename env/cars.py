# Looping through on Entire List
magicians = ['david', 'willow', 'greg']
# Store Value in magician
for magician in magicians:
    print(magician.title() + ", that was a geat trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
    print("Thank you, everyone. That was a great magic show!")

    for value in range(1, 40):
        print(value)
numbers = list(range(1,6))
# slicing a List
players = ['willow', 'james', 'adeyemi', 'oshimen', 'tinubu']
print(players[1:6])