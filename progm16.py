 #Rock Paper Scissors Game – Determine winner between user and computer.
import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter rock, paper, or scissors: ").lower()
if user_choice == computer_choice:

    print(f"Both chose {user_choice}. It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
elif user_choice in choices:    
    print(f"You chose {user_choice} and the computer chose {computer_choice}. Computer wins!")  
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")
        