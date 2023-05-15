# Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
# Adding New Key-Value Pairs
print(alien_0)
# Positioning alien left edge of the screen
# the x-cordinate to 0 and 25 pixels from to by setting -y to positive
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# Modifying Values in a Dictionary
alien_0['color'] = 'yellow'
print("The alien is now  " + alien_0['color'] + ".")

# Accessing Values in a Dictionary
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] == alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
