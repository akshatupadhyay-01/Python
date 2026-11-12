import random

emojis = {
    "r": "✊",
    "p": "✋",
    "s": "✌️"
}
choose = ("r", "p", "s")

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, Scissors (r/p/s): ").lower()

        if user_choice in choose:
            return user_choice
        
        else:
            print("Invalid Choice")
    
def display_choice(user_choice, computer_choice):
    print(f"User Choice: {emojis[user_choice]}")
    print(f"Computer Choice: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
    (user_choice == "r" and computer_choice == "s") or 
    (user_choice == "s" and computer_choice == "p") or 
    (user_choice == "p)" and computer_choice == "r")):
        print("You win!")

    else:
        print("Computer wins!")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choose)

        display_choice(user_choice, computer_choice) 

        determine_winner(user_choice, computer_choice) 

        should_continue = input("Coninue? (y/n): ").lower()
        if should_continue == 'n':
            break
    
play_game()

