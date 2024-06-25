import tkinter as tk
from tkinter import messagebox
import random

# Function to get computer choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play a round of the game
def play_round(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")
    
    # Update scores
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    score_label.config(text=f"Scores -> You: {user_score}, Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice to start the game.")
    score_label.config(text=f"Scores -> You: {user_score}, Computer: {computer_score}")

# Set up the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Create and place widgets
tk.Label(root, text="Rock, Paper, Scissors", font=('Helvetica', 16, 'bold')).pack(pady=10)

result_label = tk.Label(root, text="Make your choice to start the game.", font=('Helvetica', 12))
result_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

rock_button = tk.Button(frame, text="Rock", command=lambda: play_round('rock'))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(frame, text="Paper", command=lambda: play_round('paper'))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(frame, text="Scissors", command=lambda: play_round('scissors'))
scissors_button.grid(row=0, column=2, padx=5)

score_label = tk.Label(root, text=f"Scores -> You: {user_score}, Computer: {computer_score}", font=('Helvetica', 12))
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Run the application
root.mainloop()
