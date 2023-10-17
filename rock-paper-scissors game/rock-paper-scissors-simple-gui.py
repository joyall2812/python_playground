import tkinter as tk
import random

def set_max_score():
    global max_score
    max_score = int(max_score_entry.get())

def user_choice(user_pick):
    global user_score, computer_score, max_score
    if user_score < max_score and computer_score < max_score:
        computer_pick = random.choice(choices)
        computer_label.config(text=f'Computer picked: {computer_pick}')

        if user_pick == 'rock' and computer_pick == 'scissors':
            user_score += 1
            user_score_label.config(text=f'Your Score: {user_score}')
            outcome_label.config(text='You won this round! 🤺')
        elif user_pick == 'scissors' and computer_pick == 'paper':
            user_score += 1
            user_score_label.config(text=f'Your Score: {user_score}')
            outcome_label.config(text='You won this round! 🤺')
        elif user_pick == 'paper' and computer_pick == 'rock':
            user_score += 1
            user_score_label.config(text=f'Your Score: {user_score}')
            outcome_label.config(text='You won this round! 🤺')
        elif user_pick == computer_pick:
            outcome_label.config(text='That\'s a draw! 🤝')
        else:
            computer_score += 1
            computer_score_label.config(text=f'Computer Score: {computer_score}')
            outcome_label.config(text='Computer scored! 😎')

        if user_score == max_score:
            outcome_label.config(text='You won the game! 🙌')
            user_button_rock.config(state='disabled')
            user_button_paper.config(state='disabled')
            user_button_scissors.config(state='disabled')
        elif computer_score == max_score:
            outcome_label.config(text='Computer won the game! 😎')
            user_button_rock.config(state='disabled')
            user_button_paper.config(state='disabled')
            user_button_scissors.config(state='disabled')

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

user_score = 0
computer_score = 0
max_score = 3
choices = ['rock', 'paper', 'scissors']

user_score_label = tk.Label(root, text=f'Your Score: {user_score}')
user_score_label.pack()
computer_score_label = tk.Label(root, text=f'Computer Score: {computer_score}')
computer_score_label.pack()

computer_label = tk.Label(root, text='Computer picked: ?')
computer_label.pack()
outcome_label = tk.Label(root, text='')
outcome_label.pack()

max_score_label = tk.Label(root, text='Enter Max Score:')
max_score_label.pack()
max_score_entry = tk.Entry(root)
max_score_entry.pack()
max_score_button = tk.Button(root, text='Set Max Score', command=set_max_score)
max_score_button.pack()

user_button_rock = tk.Button(root, text="Rock", command=lambda: user_choice('rock'))
user_button_rock.pack()
user_button_paper = tk.Button(root, text="Paper", command=lambda: user_choice('paper'))
user_button_paper.pack()
user_button_scissors = tk.Button(root, text="Scissors", command=lambda: user_choice('scissors'))
user_button_scissors.pack()

root.mainloop()
