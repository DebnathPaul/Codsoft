

import random

def get_user_choice():
    user_choice = input("Please enter in 'CAPITAL LETTER' \nPlease enter your choice (ROCK, PAPER, SCISSORS): ")
    while user_choice not in ['ROCK', 'PAPER', 'SCISSORS']:
        print("Invalid choice. \nPlease try again.")
        user_choice = input("Please enter in 'CAPITAL LETTER' \nPlease enter your choice (rock, paper, scissors): ")
    return user_choice

def get_computer_choice():
    choices = ['ROCK', 'PAPER', 'SCISSORS']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Both of you chose same item. So, It's a tie."
    elif (user_choice == 'ROCK' and computer_choice == 'SCISSORS') or \
         (user_choice == 'SCISSORS' and computer_choice == 'PAPER') or \
         (user_choice == 'PAPER' and computer_choice == 'ROCK'):
        return "Congratulation, You won."
    else:
        return "Oops! You lose."

def ABCD():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "Congratulation, You won.":
            user_score += 1
        elif result == "Oops! You lose.":
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (YES / NO): ").lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing these game. ")
    print(f"You final Scores is : {user_score}\nComputer final Scores is : {computer_score}")

ABCD()
















    
