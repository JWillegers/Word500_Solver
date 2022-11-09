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
    window = tk.Tk(className='Word500 solver by JWillegers')  # create window
    window.geometry(str(width) + 'x' + str(height))
    window.resizable(False, False)
    window.configure(bg=bg_color)

    home_screen(window)
    window.mainloop() #show window (and interact with it)


def home_screen(window):
    global middle_frame
    middle_frame = tk.Frame(window, bg=bg_color)
    middle_frame.pack()

    greeting = tk.Label(middle_frame, text='Word500 solver by JWillegers', font=('Arial', int(height / 20)), fg=txt_color, bg=bg_color)
    greeting.pack(pady=int(height/50))

    select = tk.Label(middle_frame, text='Start by selecting a difficulty', font=('Arial', int(height / 40)), fg=txt_color, bg=bg_color)
    select.pack(pady=int(height/50))

    button_easy = tk.Button(
        middle_frame,
        text='Easy',
        width=20,
        height=2,
        command=easy,
        font=('Arial', int(height/50)),
        fg=color4,
        bg=input_color
    )
    button_easy.pack(pady=int(height/50))

    button_medium = tk.Button(
        middle_frame,
        text='Medium',
        width=20,
        height=2,
        command=medium,
        font=('Arial', int(height / 50)),
        fg=color4,
        bg=input_color
    )
    button_medium.pack(pady=int(height/50))
    button_hard = tk.Button(
        middle_frame,
        text='Hard',
        width=20,
        height=2,
        command=hard,
        font=('Arial', int(height / 50)),
        fg=color4,
        bg=input_color
    )
    button_hard.pack(pady=int(height/50))


def easy():
    start_game('easy')


def medium():
    start_game('medium')


def hard():
    start_game('hard')


def start_game(difficulty):
    allowed_words, words_still_possible = prepare_game.get_words(difficulty)
    build_game_screen()


def build_game_screen():
    #first remove all old widgets
    for widget in middle_frame.winfo_children():
        widget.destroy()

run()
