alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
newpoint = alien_0['points']
print("You have earned " + str(newpoint) + " points")
alien_0['x_point'] = 0
alien_0['y_point'] = 25
print(alien_0)
alien_0['color'] = 'red'
print(alien_0)
del alien_0['color']
print(alien_0)
