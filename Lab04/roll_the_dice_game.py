import roll_the_dice as roll

# Get gamers' names
player1 = input('Enter name for player one:\n')
player2 = input('Enter name for player two:\n')

# Use the function defined in another module
# The function takes two parameters: names of the players
roll.roll_the_dice(player1, player2)


