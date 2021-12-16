import roll_the_dice as roll
import get_names as gn

# Get gamers' names
names = gn.get_gamers_names()
player1 = names[0]
player2 = names[1]

# Use the function defined in another module
# The function takes two parameters: names of the players
roll.roll_the_dice(player1, player2)


