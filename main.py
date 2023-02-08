import json
import math
import threading
import tkinter as tk
import solver
import time
from preparation import first_guess
from preparation import lookup_table
from preparation import frequencies
from os import path


# change these number for changing screen size
# warning: some stuff might overlap if numbers are too small
width = 1600
height = 900

# global variables
allowed_words = {}
words_still_possible = {}
loaded_second_guess = {}
lookup = None
label_mistake = None
left_list = None
right_frame_label = None
word_sigmoid = None
word_freq = None
difficulty = None
thread_is_running = False
block_typing = False
right_frame_text = ''
guess_counter = 0
uncertainty = 0

bg_color = '#121212'
txt_color = '#A27B5C'
input_bg_color = '#2C3639'
input_txt_color = '#DCD7C9'


def run():
    # configure GUI
    global window
    window = tk.Tk(className='Word500 solver by Jonathan Willegers')  # create window
    window.geometry(str(width) + 'x' + str(height))
    window.resizable(False, False)
    window.configure(bg=bg_color)
    window.bind('<Return>', check_guess)

    # start GUI
    window.after(200, home_screen)
    window.mainloop()  # show window (and interact with it)


def home_screen():
    global home_frame
    global thread_is_running
    home_frame = tk.Frame(window, bg=bg_color)
    home_frame.pack()

    home_frame.rowconfigure(8, weight=1)
    home_frame.columnconfigure(0, weight=1)
    home_frame.columnconfigure(1, weight=1)
    home_frame.columnconfigure(4, weight=1)

    label_empty1 = tk.Label(home_frame, text=' ', bg=bg_color, fg=bg_color)
    label_empty1.grid(row=0, columnspan=5, pady=20)

    greeting = tk.Label(home_frame, text='Word500 solver', font=('Arial', int(height / 15)),
                        fg=txt_color, bg=bg_color, anchor='center')
    greeting.grid(row=1, columnspan=5, pady=20)

    credit = tk.Label(home_frame, text='by Jonathan Willegers', font=('Arial', int(height / 40)),
                      fg=txt_color, bg=bg_color, anchor='center')
    credit.grid(row=2, columnspan=5)

    label_empty2 = tk.Label(home_frame, text=' ', bg=bg_color, fg=bg_color)
    label_empty2.grid(row=3, columnspan=5, pady=20)

    # load lookup table
    if lookup is None:
        thread = threading.Thread(target=thread_lookup, daemon=True)
        thread_is_running = True
        max_dots = 6
        dot_counter = 1
        thread.start()
        loading = tk.Label()
        while thread_is_running:
            loading.destroy()
            dots = ''
            for d in range(dot_counter):
                dots += '.'
            for space in range(max_dots - len(dots)):
                dots += ' '
            spaces = ' '*max_dots  # spaces to center text
            loading = tk.Label(home_frame, text=spaces + 'Loading files' + dots, font=('Arial', int(height / 25)),
                               fg=txt_color, bg=bg_color, anchor='center')
            loading.grid(row=4, columnspan=5, pady=15)
            dot_counter += 1
            dot_counter = dot_counter % max_dots
            window.update()
            time.sleep(0.25)
        loading.destroy()

    select = tk.Label(home_frame, text='Start by selecting a difficulty', font=('Arial', int(height / 25)),
                      fg=txt_color, bg=bg_color, anchor='center')
    select.grid(row=4, columnspan=5, pady=15)

    button_easy = tk.Button(
        home_frame,
        text='Easy',
        width=20,
        height=2,
        command=easy,
        font=('Arial', int(height / 50)),
        fg=input_txt_color,
        bg=input_bg_color
    )
    button_easy.grid(row=5, column=2, pady=5)
    label_easy = tk.Label(
        home_frame,
        text='- No JQXZ\n- No repeat letters',
        font=('Arial', int(height / 60)),
        bg=bg_color,
        fg=txt_color,
    )
    label_easy.grid(row=5, column=3, padx=5)

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
    button_medium.grid(row=6, column=2, pady=5)
    label_medium = tk.Label(
        home_frame,
        text='- No repeat letters',
        font=('Arial', int(height / 60)),
        bg=bg_color,
        fg=txt_color,
    )
    label_medium.grid(row=6, column=3, padx=5)


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
    button_hard.grid(row=7, column=2, pady=5)
    window.update()


def thread_lookup():
    global lookup
    global thread_is_running
    global word_sigmoid
    global word_freq
    lookup = lookup_table.load_lookup_table(False)
    word_sigmoid = frequencies.get_sigmoid()
    word_freq = frequencies.get_frequencies()
    thread_is_running = False


def easy():
    global difficulty
    difficulty = 'easy'
    start_game()


def medium():
    global difficulty
    difficulty = 'medium'
    start_game()


def hard():
    global difficulty
    difficulty = 'hard'
    start_game()


# load necessary .txt files
def start_game():
    global allowed_words
    global words_still_possible
    global difficulty
    global block_typing
    words_still_possible = first_guess.load_words(difficulty)
    words_still_possible = dict(sorted(words_still_possible.items(), key=lambda item: item[1], reverse=True)) # sort by entropy decreasing
    with open('preparation/allowed_words.txt', 'r') as file:
        allowed_words = file.read().split('\n')
    block_typing = False
    build_game_screen()


def build_game_screen():
    # first remove all old widgets
    home_frame.destroy()

    global middle_frame
    global right_frame
    global left_frame
    global right_frame_text

    # making frames
    # sticky makes background fill the whole frame
    left_frame = tk.Frame(window, bg=bg_color)
    left_frame.grid(row=0, column=0, sticky='nesw')
    middle_frame = tk.Frame(window, bg=bg_color)
    middle_frame.grid(row=0, column=1, sticky='nesw')
    right_frame = tk.Frame(window, bg=bg_color)
    right_frame.grid(row=0, column=2, sticky='nesw')

    # configuring columns and rows such that they fill the whole window
    window.columnconfigure(0, weight=3)
    window.columnconfigure(1, weight=3)
    window.columnconfigure(2, weight=2)
    window.rowconfigure(0, weight=1)

    right_title = tk.Label(
        right_frame,
        text='Uncertainty after guesses',
        bg=bg_color,
        fg=txt_color,
        font=('Arial', int(height / 40))
    )
    right_title.pack(pady=int(height / 20))
    left_title = tk.Label(
        left_frame,
        text='Guess suggestions',
        bg=bg_color,
        fg=txt_color,
        font=('Arial', int(height / 40))
    )
    left_title.pack(pady=(int(height / 20), 5))
    left_sub_title = tk.Label(
        left_frame,
        text='with entropy and likeliness',
        bg=bg_color,
        fg=txt_color,
        font=('Arial', int(height / 50))
    )
    left_sub_title.pack(pady=(5, int(height / 50)))
    create_middle_frame()
    update_right_frame('')
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
        font=('Arial', int(height / 30)),
    )
    middle_title.grid(row=0, columnspan=column_max + 1, pady=int(height / 20))

    global entry_boxes
    entry_boxes = []
    vcmd_char = (window.register(validate_letter), '%P')
    vcmd_digit = (window.register(validate_digit), '%P')

    # creating input frames for letters and numbers
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
            if column < 7:
                v = vcmd_char
            else:
                v = vcmd_digit

            if column != 6:
                entry = tk.Entry(middle_frame, fg=fg, bg=bg, width=4, font=('Arial', int(height / 50)),
                                 justify=tk.CENTER, validate='key', validatecommand=v,
                                 disabledforeground=fg, disabledbackground=bg)
                entry.grid(row=row, column=column, padx=2, pady=5, ipady=10)
                entry_row.append(entry)
        entry_boxes.append(entry_row)

    # creating guess counter to keep track of how many guesses are done
    global guess_counter
    guess_counter = 0

    # adding invisible label with the longest message to keep spacing consistent
    msg = 'Numbers in the green, yellow and red box should add up to 5'
    spaces = tk.Label(middle_frame, text=msg, bg=bg_color, fg=bg_color,
                      font=('Arial', int(height / 50)), justify=tk.CENTER)
    spaces.grid(row=10, columnspan=column_max + 1)

    # spacing
    middle_frame.columnconfigure(0, weight=5)
    middle_frame.columnconfigure(6, weight=1)
    middle_frame.columnconfigure(column_max, weight=5)


def validate_letter(P):
    global entry_boxes
    global guess_counter
    global block_typing
    if not block_typing:
        if len(P) == 0:
            return True
        elif len(P) == 1 and not P.isdigit():
            # go to next entry
            for i in range(len(entry_boxes[guess_counter]) - 1):
                if len(entry_boxes[guess_counter][i].get()) == 0:
                    entry_boxes[guess_counter][i + 1].focus_set()
                    break
            return True
    return False


def validate_digit(P):
    global entry_boxes
    global guess_counter
    global block_typing
    if not block_typing:
        if len(P) == 0:
            # empty Entry is okay
            return True
        elif len(P) == 1 and P.isdigit():
            # go to next entry
            for i in range(len(entry_boxes[guess_counter]) - 1):
                if len(entry_boxes[guess_counter][i].get()) == 0:
                    entry_boxes[guess_counter][i + 1].focus()
                    break
            return True
    return False


def update_left_frame():
    global left_list
    global uncertainty
    if left_list is not None:
        left_list.destroy()
    left_list = tk.Frame(left_frame, bg=bg_color)
    left_list.pack()
    suggestions = solver.give_n_suggestions(int(height / 40), words_still_possible, word_freq, word_sigmoid, guess_counter, uncertainty)
    for i in range(len(suggestions)):
        word, entropy, probability = suggestions[i]
        label_word = tk.Label(
            left_list,
            text=word,
            bg=bg_color,
            fg=txt_color,
            font=('Arial', int(height / 50)),
            justify=tk.CENTER
        )
        label_word.grid(row=i, column=0)
        label_entropy = tk.Label(
            left_list,
            text=str(entropy),
            bg=bg_color,
            fg=txt_color,
            font=('Arial', int(height / 50)),
            justify=tk.CENTER
        )
        label_entropy.grid(row=i, column=1, padx=int(width / 75))
        label_prob = tk.Label(
            left_list,
            text=str(probability) + '%' if probability >= 0.1 else '<0.1%',
            bg=bg_color,
            fg=txt_color,
            font=('Arial', int(height / 50)),
            justify=tk.CENTER
        )
        label_prob.grid(row=i, column=2)


def update_right_frame(guess):
    global right_frame_text
    global words_still_possible
    global right_frame_label
    global right_frame
    global uncertainty
    uncertainty = 0
    max_uncertainty = 0
    for word in words_still_possible:
        max_uncertainty += word_sigmoid[word]
    for word in words_still_possible:
        px = word_sigmoid[word] / max_uncertainty
        uncertainty += px * math.log2(1/px)

    if right_frame_label is not None:
        right_frame_label.destroy()
    if right_frame_text == '':
        right_frame_text = 'No guesses: ' + str(round(uncertainty, 2)) + '\n\n'
    elif len(words_still_possible.keys()) == 1:
        right_frame_text += guess + ': 0.0\n\n'
    else:
        right_frame_text += guess + ': ' + str(round(uncertainty, 2)) + '\n\n'
    right_frame_label = tk.Label(right_frame, text=right_frame_text, font=('Arial', int(height / 50)), bg=bg_color, fg=txt_color)
    right_frame_label.pack()


def check_guess(event):
    # getting global variables
    global entry_boxes
    global column_max
    global label_mistake
    global words_still_possible
    global block_typing
    if not block_typing:
        if 'middle_frame' in globals() and 'guess_counter' in globals():  # checking if we are not on main screen
            global guess_counter
            mistake_found = False
            box_counter = 0  # input box
            msg = ''  # error message
            word = ''  # guessed word
            green = 0
            yellow = 0
            red = 0
            if not label_mistake == None:  # destroy old label_mistake
                label_mistake.destroy()

            # checking input
            for input in entry_boxes[guess_counter]:
                if box_counter >= 5:  # check if the last 3 inputboxes are numbers
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
                else:  # add letter to word
                    word += input.get().lower()
                box_counter += 1
            # check if guess is a valid word
            if msg == '' and word not in allowed_words:
                mistake_found = True
                msg = 'Not a valid word'
            # check that green + yellow + red = 5
            elif msg == '' and green + yellow + red != 5:
                mistake_found = True
                msg = 'Numbers in the green, yellow and red box should add up to 5'
            # display messages or process guess
            if mistake_found:
                label_mistake = tk.Label(middle_frame, text=msg, bg=bg_color, fg=txt_color,
                                         font=('Arial', int(height / 60)))
                label_mistake.grid(row=9, columnspan=column_max + 1, pady=10)
            else:
                # lock row
                for entry in entry_boxes[guess_counter]:
                    entry.config(state='disabled')
                # process guess
                global thread_is_running
                if guess_counter == 0 and difficulty == 'hard' and path.exists('./preparation/second_guess/' + word + '.txt'):
                    thread = threading.Thread(target=thread_load_second_guess, args=(word, green, yellow, red), daemon=True)
                else:
                    thread = threading.Thread(target=thread_process_guess, args=(word, green, yellow, red), daemon=True)
                thread_is_running = True
                thread.start()
                max_dots = 6
                count_dots = 0
                processing = tk.Label()
                while thread_is_running:
                    processing.destroy()
                    dots = ''
                    for d in range(count_dots):
                        dots += '.'
                    for space in range(max_dots - count_dots):
                        dots += ' '
                    processing = tk.Label(middle_frame, text='Processing guess' + dots, bg=bg_color, fg=txt_color,
                                          font=('Arial', int(height/50)))
                    processing.grid(row=9, columnspan=column_max + 1, pady=20)
                    count_dots = (count_dots + 1) % max_dots
                    time.sleep(0.25)
                    window.update()
                processing.destroy()
                msg = ''
                long_msg = False
                if isinstance(words_still_possible, str):
                    msg = words_still_possible
                    long_msg = True
                # update window
                if msg == '':
                    update_left_frame()
                    update_right_frame(word.lower())
                    guess_counter += 1

                # check if game is over
                if green == 5:
                    msg = 'You won!'
                elif guess_counter == 8:
                    msg = 'You lost'
                if msg != '':
                    block_typing = True
                    font_size = int(height / 55) if long_msg else int(height / 40)
                    label_end_game = tk.Label(middle_frame, text=msg, bg=bg_color, fg=txt_color, font=('Arial', font_size))
                    label_end_game.grid(row=9, columnspan=column_max + 1, pady=10)
                    button_end_game = tk.Button(middle_frame, text='Home', bg=input_bg_color, fg=txt_color, font=('Arial', int(height / 40)), command=home)
                    button_end_game.grid(row=10, columnspan=column_max + 1, pady=10, ipadx=10, ipady=5)


def thread_process_guess(word, green, yellow, red):
    global words_still_possible
    global thread_is_running
    words_still_possible = solver.process_guess(word.lower(), green, yellow, red, lookup, words_still_possible, word_sigmoid)
    thread_is_running = False


def thread_load_second_guess(word, green, yellow, red):
    global words_still_possible
    global loaded_second_guess
    global thread_is_running
    code = str(green) + str(yellow) + str(red)
    if word in loaded_second_guess.keys():
        words_still_possible = loaded_second_guess[word][code]
    else:
        with open('./preparation/second_guess/' + word + '.txt', 'r') as file:
            second_guess = json.load(file)
        loaded_second_guess[word] = second_guess
        words_still_possible = second_guess[code]
    thread_is_running = False


def home():
    # destroy game screen
    global middle_frame
    global right_frame
    global left_frame
    middle_frame.destroy()
    right_frame.destroy()
    left_frame.destroy()

    # reset some global variables
    global right_frame_text
    global words_still_possible
    global left_list
    global right_frame_label
    right_frame_text = ''
    words_still_possible = {}
    left_list = None
    right_frame_label = None

    # build homescreen
    home_screen()


if __name__ == '__main__':
    run()
