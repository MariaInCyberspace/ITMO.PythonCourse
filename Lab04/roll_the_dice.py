from random import randint
import time

roll_again = False
p1_total = 0
p2_total = 0


def roll_the_dice(player1, player2):
    # To use outside of function's scope
    global p1_total, p2_total, roll_again
    # Throw imitation for player 1
    print(f'{player1} rolls the dice')
    time.sleep(2)
    n1 = randint(1, 6)
    print(f'{player1} got: {n1}')

    print()

    # Throw imitation for player 2
    print(f'{player2} rolls the dice')
    time.sleep(2)
    n2 = randint(1, 6)
    print(f'{player2} got: {n2}')

    # Update total scores for both players
    p1_total += n1
    p2_total += n2

    # Continue rolling?
    want_to_roll_again = input('\nDo you want to roll again? \nPress "Y" for yes or any other character for no\n')
    if want_to_roll_again == 'Y' or want_to_roll_again == 'y':
        roll_again = True
    else:  # Interpret the results
        print(f"{player1}'s total score: {p1_total}",
              f"{player2}'s total score: {p2_total}")
        if p1_total > p2_total:
            print(f"{player1} won!")
        elif p1_total < p2_total:
            print(f"{player2} won!")
        else:
            print("It's a tie!")
        roll_again = False

    while roll_again:
        roll_the_dice(player1, player2)  # Recursive call
