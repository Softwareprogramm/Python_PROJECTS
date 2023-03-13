# Rock, Paper, Scissor game Project
import random

# A welcome and intro to the program
game_intro = "\nWelcome Players to\n"
game_intro += "Rock, Paper, Scissor.\nEnter 'quit' to end the program!!!"
print(game_intro)

# Player will enter their name so the program can address them by their name
player_name = input("\nNow, enter your name: ").title()
print(f"Welcome {player_name}")
# List that contains the trigger words, player input and computers chose.
triggers = ["rock", "paper", "scissor"]
ai_score = 0
player_score = 0

# The conditional triggers.
# variable that will control the while loop
loop = True
while loop:

    computer_choice = random.choice(triggers)
    player = input("Choose (rock, paper, scissor): ").lower()
    if player == "quit":
        print("Goodbye, loop has ended!!!")
        loop = False
    else:
        if player not in triggers:
            print("An unknown value entered. Try again!!")
        elif player == computer_choice:
            print(f"{player_name} chose: {player} and AI chose: {computer_choice}")
            print("It's a draw.")
        elif player == "rock" and computer_choice == "paper":
            print(f"{player_name} chose: {player} and AI chose: {computer_choice}")
            print("AI wins.")
            ai_score += 1
        elif player == "rock" and computer_choice == "scissor":
            print(f"{player_name} chose: {player} and AI chose: {computer_choice}")
            print(f"{player_name} wins")
            player_score += 1
        elif player == "paper" and computer_choice == "scissor":
            print(f"{player_name} chose: {player} and AI chose: {computer_choice}")
            print("AI wins")
            ai_score += 1
        elif player == "scissor" and computer_choice == "paper":
            print(f"{player_name} chose: {player} and AI chose: {computer_choice}")
            print(f"{player_name} wins")
            player_score += 1
        elif computer_choice == "rock" and player == "paper":
            print(f"{player_name} chose: {player} and AI chose: {computer_choice}")
            print(f"{player_name} wins")
            player_score += 1
        elif player == "scissor" and computer_choice == "rock":
            print(f"{player_name} chose: {player} and AI chose: {computer_choice}")
            print(f"AI wins")
            ai_score += 1

        if player_score == 3 and ai_score < 3:
            print(f"{player_name} wins with a total of {player_score} points.")
            break
        elif ai_score == 3 and player_score < 3:
            print(f"\nAI wins with a total of {ai_score} points.")
            print(f"You have a total of {player_score} point.")
            loop = False
print(f"\nThanks {player_name} for playing!!!")
