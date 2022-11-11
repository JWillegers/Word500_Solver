import copy
import math
import tkinter as tk

import prepare_game

#change these number for changing screen size
#warning: some stuff might overlap if numbers are too small
import reduce_words

width = 1600
height = 900

#global variables
allowed_words = []
words_still_possible = []
words_entropy = []
patterns = []
label_mistake = None
left_list = None

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
    global allowed_words
    global words_still_possible
    allowed_words, words_still_possible = prepare_game.get_words(difficulty)

    #create patterns
    global patterns
    for g in range(6):
        for y in range(6-g):
            patterns.append(str(g) + ' ' + str(y) + ' ' + str(5-g-y))

    build_game_screen()

def build_game_screen():
    #first remove all old widgets
    home_frame.destroy()

    global middle_frame
    global right_frame
    global left_frame

    #making frames
    #sticky makes background fill the whole frame
    left_frame = tk.Frame(window, bg='pink')
    left_frame.grid(row=0, column=0, sticky='nesw')
    middle_frame = tk.Frame(window, bg=bg_color)
    middle_frame.grid(row=0, column=1, sticky='nesw')
    right_frame = tk.Frame(window, bg='blue')
    right_frame.grid(row=0, column=2, sticky='nesw')


    #configuring columns and rows such that they fill the whole window
    window.columnconfigure(0, weight=2)
    window.columnconfigure(1, weight=2)
    window.columnconfigure(2, weight=2)
    window.rowconfigure(0, weight=1)

    right_title = tk.Label(
        right_frame,
        text='Other',
        bg=bg_color,
        fg=txt_color
    )
    right_title.pack(pady=5)
    left_title = tk.Label(
        left_frame,
        text='Guess suggestions',
        bg=bg_color,
        fg=txt_color,
        font=('Arial', int(height / 50))
    )
    left_title.pack(pady=5)

    create_middle_frame()
    get_recommendations()
    update_left_frame()


def create_middle_frame():
    global middle_frame
    global column_max
    column_max = 12


    middle_title = tk.Label(
        middle_frame,
        text='Word500',
        bg=bg_color,
        fg=txt_color,
        font=('Arial', int(height / 50)),
    )
    middle_title.grid(row=0, columnspan=column_max + 1, pady=25)

    global entry_boxes
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
    middle_frame.columnconfigure(column_max, weight=5)

def update_left_frame():
    global left_list
    if left_list is not None:
        left_list.destroy()

    word_list = ''
    max_words = 30
    for i in range(min(len(words_entropy), max_words)):
        word_list += words_entropy[i][0] + ' ' + str(words_entropy[i][1])
        if i != min(len(words_entropy), max_words) - 1:
            word_list += '\n'
    left_list = tk.Label(left_frame, text=word_list, font=('Arial', int(height / 50)), bg=bg_color, fg=txt_color)
    left_list.pack(pady=20)

def check_guess(event):
    #getting global variables
    global entry_boxes
    global column_max
    global label_mistake

    if 'middle_frame' in globals() and 'guess_counter' in globals(): #checking if we are not on main screen
        global guess_counter
        mistake_found = False
        box_counter = 0 #input box
        msg = '' #error message
        word = '' #guessed word
        green = 0
        yellow = 0
        red = 0
        if not label_mistake == None: #destroy old label_mistake
            label_mistake.destroy()

        #cheking input
        for input in entry_boxes[guess_counter]:
            if len(input.get()) != 1: #Check that every inputbox has exactly 1 character
                mistake_found = True
                msg = 'Please enter only one character per field'
                break
            elif box_counter >= 5: #check if the last 3 inputboxes are numbers
                try:
                    match box_counter:
                        case 5:
                            green = int(input.get())
                        case 6:
                            yellow = int(input.get())
                        case 7:
                            red = int(input.get())
                except:
                    mistake_found = True
                    msg = 'Please put a number in the green, yellow, and red box'
            else: #add letter to word
                word += input.get()
            box_counter += 1
        #check if guess is a valid word
        if msg == '' and word.lower() not in allowed_words:
            mistake_found = True
            msg = 'Not a valid word'
        #check that green + yellow + red = 5
        elif msg == '' and green + yellow + red != 5:
            mistake_found = True
            msg = 'Numbers in the green, yellow and red box should add up to 5'
        #display messages or
        if mistake_found:
            label_mistake = tk.Label(middle_frame, text=msg, bg=bg_color, fg=txt_color, font=('Arial', int(height / 60)))
            label_mistake.grid(row=9, columnspan=column_max + 1, pady=10)
        else:
            process_guess(word, green, yellow, red)
            guess_counter += 1


def process_guess(word, green, yellow, red):
    global words_still_possible
    guess = word + ' ' + str(green) + ' ' + str(yellow) + ' ' + str(red)
    wordfound, words_still_possible = reduce_words.process_guess(guess, words_still_possible)
    get_recommendations()
    update_left_frame()


def get_recommendations():
    global words_still_possible
    global allowed_words
    global words_entropy
    words_entropy.clear()
    ''' 
    Entropy = E[Information] = sum p(x)*Information, all x = sum p(x)*log2(1/p(x)), all x
    where Information=log2(1/p(x))
    where p(x) is the p(x) is the change that [green, yellow, red] occurs
        p(x)=len(reduced_words_still_possible)/len(current_words_still_possible)
    '''
    lenCWSP = len(words_still_possible)
    for w in allowed_words:
        entropy = 0 #entropy for w
        wsp = copy.deepcopy(words_still_possible) #deepcopy words_still_possible
        for pattern in patterns:
            w += ' ' + pattern
            wordfound, wsp = reduce_words.process_guess(w, wsp)
            px = len(wsp) / lenCWSP
            entropy += px * math.log2(1/px)
        entropy = round(entropy, 2)
        words_entropy.append([w, entropy])


run()

