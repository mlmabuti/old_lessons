from random import randint

player_score = 0
robot_score = 0
player = input("\nType 'quit' to exit program \nEnter move: ").lower()

while player != "quit":
    robot_choice = randint(0, 2)
    rock = 0
    paper = 1
    scissors = 2
    if player and player == "rock" or player == "paper" or player == "scissors":
        if player == "rock":
            if robot_choice is paper:
                 robot_score = robot_score + 1
                 print("Robot chose PAPER!")
                 print(f"Score; Robot: {robot_score}, Player: {player_score} ")
                 player = input("\nEnter move: ").lower()
             elif robot_choice is scissors:
                 player_score = player_score + 1
                 print("Robot chose SCISSORS!")
                 print(f"Score; Robot: {robot_score}, Player: {player_score} ")
                 player = input("\nEnter move: ").lower()
             else:
                 print("Both chose ROCK, it is a DRAW!")
                 player = input("\nEnter move: ").lower()
        if player == "paper":
            if robot_choice is scissors:
                robot_score = robot_score + 1
                print("Robot chose SCISSORS!")
                print(f"Score; Robot: {robot_score}, Player: {player_score} ")
                player = input("\nEnter move: ").lower()
            elif robot_choice is rock:
                player_score = player_score + 1
                print("Robot chose ROCK")
                print(f"Score; Robot: {robot_score}, Player: {player_score} ")
                player = input("\nEnter move: ").lower()
            else:
                print("Both chose PAPER, it is a DRAW!")
                player = input("\nEnter move: ").lower()
        if player == "scissors":
            if robot_choice is rock:
                robot_score = robot_score + 1
                print("Robot chose ROCK!")
                 print(f"Score; Robot: {robot_score}, Player: {player_score} ")
                 player = input("\nEnter move: ").lower()
            elif robot_choice is paper:
                player_score = player_score + 1
                print("Robot chose PAPER!")
                 print(f"Score; Robot: {robot_score}, Player: {player_score} ")
                 player = input("\nEnter move: ").lower()
            else:
                print("Both chose SCISSORS, it is a DRAW!")
                player = input("\nEnter move: ").lower()
    else:
        print("INVALID MOVE.")
        player = input("\nEnter move: ").lower()

if player == "quit":
    if player_score > robot_score:
        print(f"\nPlayer WON with {player_score} POINTS!!")
    elif player_score == robot_score:
          print("Nobody won, DRAW!!")
    else:
        print(
            f"\nRobot WON with {robot_score} POINTS!! Better luck next time.")
        print("\nBye bye.")
