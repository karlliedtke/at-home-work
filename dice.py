import random

def rollDice():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def over_under():
    player1points = 0
    player2points = 0

    while True:
        print("\nplayer 1 is now rolling the dice")
        roll = rollDice()
        print(roll)
        while True:
            guess = input("Player 2, will next roll be over or under? over/under: ").strip().lower()
            if guess in ["over", "under"]:
                  break
            else:
                print("Invalid input, please enter 'over' or 'under'")
        roll_two = rollDice()
        print(roll_two)
        if guess == "over" and roll_two > roll:
            player2points += 1
            print(f"\nplayer 1: {player1points} points")
            print(f"player 2: {player2points} points")
        elif guess == "under" and roll_two < roll:
                player2points += 1
                print(f"\nplayer 1: {player1points} points")
                print(f"player 2: {player2points} points")
        else:
            print("\nNo points awarded")
            print(f"player 1: {player1points} points")
            print(f"player 2: {player2points} points")

        if player2points ==6:
                print("Game over, player 2 wins")
                break
        else:
                print("turn is over, switch player roles")

        print("\nplayer 2 is now rolling the dice")
        roll = rollDice()
        print(roll)
        while True:
            guess = input("Player 2, will next roll be over or under? over/under: ").strip().lower()
            if guess in ["over", "under"]:
                  break
            else:
                print("Invalid input, please enter 'over' or 'under'")
        roll_two = rollDice()
        print(roll_two)
        if guess == "over" and roll_two > roll:
            player1points += 1
            print(f"\nplayer 1: {player1points} points")
            print(f"player 2: {player2points} points")
        elif guess == "under" and roll_two < roll:
                player1points += 1
                print(f"\nplayer 1: {player1points} points")
                print(f"player 2: {player2points} points")
        else:
            print("\nNo points awarded")
            print(f"player 1: {player1points} points")
            print(f"player 2: {player2points} points")

        if player1points ==6:
                print("Game over, player 1 wins")
                break
        else:
                print("turn is over, switch player roles")

over_under()


