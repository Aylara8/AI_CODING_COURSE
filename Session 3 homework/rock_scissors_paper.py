import random

def get_computer_choice():
    """Randomly selects rock, paper, or scissors."""
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    """Prompt user and validate input using a loop."""
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower().strip()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice. Please try again.")

def determine_winner(player, computer):
    """Uses logic to decide the outcome of a single round."""
    if player == computer:
        return "tie"
    
    # Winning conditions for the player
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if win_conditions[player] == computer:
        return "player"
    else:
        return "computer"

def play_round():
    """Coordinates a single round and returns the winner."""
    p_choice = get_player_choice()
    c_choice = get_computer_choice()
    
    print(f"Computer chose: {c_choice}")
    
    winner = determine_winner(p_choice, c_choice)
    
    if winner == "tie":
        print("It's a draw!")
    else:
        print(f"{winner.capitalize()} wins this round!")
    
    return winner

def play_tournament():
    """Manages multiple rounds and tracks the score."""
    player_score = 0
    computer_score = 0
    rounds_to_win = 2 # Best of 3
    
    print("--- Welcome to the RPS Tournament (Best of 3) ---")
    
    while player_score < rounds_to_win and computer_score < rounds_to_win:
        result = play_round()
        
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
            
        print(f"Score: You {player_score} - {computer_score} CPU\n")

    if player_score > computer_score:
        print("Congratulations! You won the tournament!")
    else:
        print("The machines have won this time.")

if __name__ == "__main__":
    play_tournament()

# Why did you split it into these specific functions?
# If I want to change the game to "Rock Paper Scissors Lizard Spock" later, I only have to update the logic function, not the whole program.
# What's one function that took multiple tries to get right?
# determine_winner, def functions.
# How did using functions make your code better?
# If the game broke, I knew exactly which function to investigate.
# What AI prompt helped you organize? 
# I want to build a Rock Paper Scissors game in Python. 