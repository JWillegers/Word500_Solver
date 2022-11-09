import tkinter as tk
import prepare_game

#change these number for changing screen size
#warning: some stuff might overlap if numbers are too small
width = 1600
height = 900

allowed_words = []
words_still_possible = []

bg_color = '#121212'
txt_color = '#A27B5C'
input_color = '#2C3639'
color4 = '#DCD7C9'

def run():
    window = tk.Tk(className='Word500 solver by JWillegers') #create window
    window.geometry(str(width) + 'x' + str(height))
    window.resizable(False, False)
    window.configure(bg=bg_color)

    home_screen()
    window.mainloop() #show window (and interact with it)

def home_screen():
    greeting = tk.Label(text='Word500 solver by JWillegers', font=('Arial', int(height / 20)), fg=txt_color, bg=bg_color)
    greeting.place(relx=0.5, rely=0.1, anchor='center')  # add to window

    select = tk.Label(text='Start by selecting a difficulty', font=('Arial', int(height / 40)), fg=txt_color, bg=bg_color)
    select.place(relx=0.5, rely=0.25, anchor='center')  # add to window

    button_easy = tk.Button(
        text='Easy',
        width=20,
        height=2,
        command=easy,
        font=('Arial', int(height/50)),
        fg=color4,
        bg=input_color
    )
    button_easy.place(relx=0.5, rely=0.4, anchor='center')

    button_medium = tk.Button(
        text='Medium',
        width=20,
        height=2,
        command=medium,
        font=('Arial', int(height / 50)),
        fg=color4,
        bg=input_color
    )
    button_medium.place(relx=0.5, rely=0.55, anchor='center')
    button_hard = tk.Button(
        text='Hard',
        width=20,
        height=2,
        command=hard,
        font=('Arial', int(height / 50)),
        fg=color4,
        bg=input_color
    )
    button_hard.place(relx=0.5, rely=0.7, anchor='center')

    button_rule_1 = tk.Label(
        text='- No JQXZ',
        font=('Arial', int(height / 70)),
        fg=color4,
        bg=bg_color
    )
    button_rule_1.place(relx=0.6, rely=0.37)

    button_rule_2 = tk.Label(
        text='- No repeat letters',
        font=('Arial', int(height / 70)),
        fg=color4,
        bg=bg_color
    )
    button_rule_2.place(relx=0.6, rely=0.4)

    button_rule_3 = tk.Label(
        text='- No repeat letters',
        font=('Arial', int(height / 70)),
        fg=color4,
        bg=bg_color
    )

    button_rule_3.place(relx=0.6, rely=0.53)


def easy():
    start_game('easy')

def medium():
    start_game('medium')

def hard():
    start_game('hard')

def start_game(difficulty):
    allowed_words, words_still_possible = prepare_game.get_words(difficulty)


run()
