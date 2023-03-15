import random
def main():
        player1 = 0
        player2 = 0
        rounds = 1

        while rounds != 4:
            print("Round" + str(rounds))
            player1 = dice_roll()
            player2 = dice_roll()
            print()
            print("Player 1:" + str(player1))
            print()
            print("Player 2:" + str(player2))
            print()
            rounds = rounds + 1

def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll



main()
