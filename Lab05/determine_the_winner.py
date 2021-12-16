
def determine_who_won(player1, player2, p1_total, p2_total):
    print(f"{player1}'s total score: {p1_total}",
          f"{player2}'s total score: {p2_total}")
    if p1_total > p2_total:
        print(f"{player1} won!")
    elif p1_total < p2_total:
        print(f"{player2} won!")
    else:
        print("It's a tie!")