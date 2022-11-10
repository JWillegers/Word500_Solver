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
input_bg_color = '#2C3639'
input_txt_color = '#DCD7C9'

def run():
    global window
    window = tk.Tk(className='Word500 solver by JWillegers')  # create window
    window.geometry(str(width) + 'x' + str(height))
    window.resizable(False, False)
    window.configure(bg=bg_color)
    window.bind('<Return>', check_guess)

    home_screen()
    window.mainloop() #show window (and interact with it)


def home_screen():
    global home_frame
    home_frame = tk.Frame(window, bg=bg_color)
    home_frame.pack()

    greeting = tk.Label(home_frame, text='Word500 solver by JWillegers', font=('Arial', int(height / 20)), fg=txt_color, bg=bg_color)
    greeting.pack(pady=int(height/50))

    select = tk.Label(home_frame, text='Start by selecting a difficulty', font=('Arial', int(height / 40)), fg=txt_color, bg=bg_color)
    select.pack(pady=int(height/50))

    button_easy = tk.Button(
        home_frame,
        text='Easy',
        width=20,
        height=2,
        command=easy,
        font=('Arial', int(height/50)),
        fg=input_txt_color,
        bg=input_bg_color
    )
    button_easy.pack(pady=int(height/50))

    button_medium = tk.Button(
        home_frame,
        text='Medium',
        width=20,
        height=2,
        command=medium,
        font=('Arial', int(height / 50)),
        fg=input_txt_color,
        bg=input_bg_color
    )
    button_medium.pack(pady=int(height/50))
    button_hard = tk.Button(
        home_frame,
        text='Hard',
        width=20,
        height=2,
        command=hard,
        font=('Arial', int(height / 50)),
        fg=input_txt_color,
        bg=input_bg_color
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
    home_frame.destroy()

    global middle_frame
    global right_frame
    global left_frame

    #making frames
    #sticky makes background fill the whole frame
    right_frame = tk.Frame(window, bg='blue')
    right_frame.grid(row=0, column=0, sticky='nesw')
    middle_frame = tk.Frame(window, bg=bg_color)
    middle_frame.grid(row=0, column=1, sticky='nesw')
    left_frame = tk.Frame(window, bg='pink')
    left_frame.grid(row=0, column=2, sticky='nesw')

    #configuring columns and rows such that they fill the whole window
    window.columnconfigure(0, weight=2)
    window.columnconfigure(1, weight=2)
    window.columnconfigure(2, weight=2)
    window.rowconfigure(0, weight=1)

    right_title = tk.Label(
        right_frame,
        text='Guess suggestions',
        bg=bg_color,
        fg=txt_color
    )
    right_title.pack(pady=5)
    left_title = tk.Label(
        left_frame,
        text='Other',
        bg=bg_color,
        fg=txt_color
    )
    left_title.pack(pady=5)

    create_middle_frame()

def create_middle_frame():
    row_max = 11
    middle_title = tk.Label(
        middle_frame,
        text='Word500',
        bg=bg_color,
        fg=txt_color,
        font=('Arial', int(height / 50)),
    )
    middle_title.grid(row=0, columnspan=row_max + 1, pady=25)

    entry_boxes = []

    #creating input frames for letters and numbers
    for row in range(1, 9):
        entry_row = []
        for column in range(1, 10):
            bg = input_bg_color
            fg = input_txt_color
            if column == 7:
                bg = 'green'
                fg = 'black'
            elif column == 8:
                bg = 'yellow'
                fg = 'black'
            elif column == 9:
                bg = 'red'
                fg = 'black'

            if column != 6:
                entry = tk.Entry(middle_frame, fg=fg, bg=bg, width=4, font=('Arial', int(height / 50)), justify=tk.CENTER)
                entry.grid(row=row, column=column, padx=2, pady=5, ipady=10)
                entry_row.append(entry)
        entry_boxes.append(entry_row)

    #creating guess counter to keep track of how many guesses are done
    global guess_counter
    guess_counter = 0

    #spacing
    middle_frame.columnconfigure(0, weight=5)
    middle_frame.columnconfigure(6, weight=1)
    middle_frame.columnconfigure(row_max, weight=5)

def check_guess():
    if 'middle_frame' in globals() and 'guess_counter' in globals(): #checking if we are not on main screen
        print('hi')


run()
