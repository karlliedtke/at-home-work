import random
def rolldice():
    player1count = 0
    player2count = 0
    while True:
        print(f"\nPlayer 1 is now rolling the dice")
        rolls = [random.randint(1,6) for i in range(5)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player1count += lowest
        print(f"player1count: {player1count}")
        if player1count >= 20:
            print("Player 1 loses, player 2 wins")
            break

        rolls = [random.randint(1,6) for i in range(4)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player1count += lowest
        print(f"player1count: {player1count}")
        if player1count >= 20:
            print("Player 1 loses, player 2 wins")
            break

        rolls = [random.randint(1,6) for i in range(3)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player1count += lowest
        print(f"player1count: {player1count}")
        if player1count >= 20:
            print("Player 1 loses, player 2 wins")
            break

        rolls = [random.randint(1,6) for i in range(2)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player1count += lowest
        print(f"player1count: {player1count}")
        if player1count >= 20:
            print("Player 1 loses, player 2 wins")
            break

        rolls = [random.randint(1,6) for i in range(1)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player1count += lowest
        print(f"player1count: {player1count}")
        if player1count >= 20:
            print("Player 1 loses, player 2 wins")
            break
        while True:
            switch = input("turn is over, switch player roles. enter yes to continue: ").strip().lower()
            if switch in ["yes"]:
                break
            else:
                print("Invalid input, please enter 'yes'")
        
        print(f"\nPlayer 2 is now rolling the dice")

        rolls = [random.randint(1,6) for i in range(5)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player2count += lowest
        print(f"player2count: {player2count}")
        if player2count >= 20:
            print("Player 2 loses, player 1 wins")
            break

        rolls = [random.randint(1,6) for i in range(4)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player2count += lowest
        print(f"player2count: {player2count}")
        if player2count >= 20:
            print("Player 2 loses, player 1 wins")
            break

        rolls = [random.randint(1,6) for i in range(3)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player2count += lowest
        print(f"player2count: {player2count}")
        if player2count >= 20:
            print("Player 2 loses, player 1 wins")
            break

        rolls = [random.randint(1,6) for i in range(2)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player2count += lowest
        print(f"player2count: {player2count}")
        if player2count >= 20:
            print("Player 2 loses, player 1 wins")
            break

        rolls = [random.randint(1,6) for i in range(1)]
        print(f"\n{rolls}")
        lowest = (min(rolls))
        print(f"lowest roll: {lowest}")
        player2count += lowest
        print(f"player2count: {player2count}")
        if player2count >= 20:
            print("Player 2 loses, player 1 wins")
            break

rolldice()