"""Solution - Exercise 5: Rock, Paper, Scissors (with the r/p/s bonus)"""

import random


def winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "player"
    return "computer"


def get_choice():
    while True:
        choice = input("rock, paper, or scissors? ").lower()
        if choice == "r":
            choice = "rock"
        elif choice == "p":
            choice = "paper"
        elif choice == "s":
            choice = "scissors"

        if choice == "rock" or choice == "paper" or choice == "scissors":
            return choice
        print("  Invalid choice, try again.")


player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    player = get_choice()
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"  You: {player}   Computer: {computer}")

    result = winner(player, computer)
    if result == "player":
        player_wins += 1
        print("  You win this round!")
    elif result == "computer":
        computer_wins += 1
        print("  Computer wins this round.")
    else:
        print("  Tie!")
    print(f"  Score: You {player_wins} - {computer_wins} Computer\n")

if player_wins == 2:
    print("You won the match!")
else:
    print("The computer won the match. Rematch?")
