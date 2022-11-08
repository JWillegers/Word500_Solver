import prepare_game
import reduce_words


def start_game():
    #asking for difficulty
    input_accepted = False
    while not input_accepted:
        difficulty = input('Which difficult do you want to play on? (easy/medium/hard)')
        input_accepted = difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard'
        if not input_accepted:
            print('Input not accepted, please try again')
    #prepare game
    possible_words, possible_words = prepare_game.get_words(difficulty)
    word_found = False
    turn_counter = 1
    #playing the game
    while not word_found and turn_counter <= 8:
        input_accepted = False
        #ask for word and colors
        while not input_accepted:
            guess = input('What did you guess? answer format: word [space] amount green [space] amount yellow [space] amount red')
            split = guess.split(' ')
            try:
                if not len(split[0]) == 5:
                    print('please enter a 5 letter word. Try again')
                elif not (int(split[1]) + int(split[2]) + int(split[3]) == 5):
                    print('the amount of green, yellow, and red should add up to 5. Try again')
                else:
                    input_accepted = True
            except IndexError:
                print('Make sure your input follows the correct format, example: house 1 1 3\nTry again')
            except ValueError:
                print('Make sure the \"amount [color]\" is a number. Try again')

        #process guess
        word_found, possible_words = reduce_words.process_guess(guess, possible_words)
        turn_counter += 1
        if not word_found:
            if len(possible_words) > 20:
                print(len(possible_words), 'left')
            else:
                s = 'words left: '
                for w in possible_words:
                    s += w + ' '
                print(s)
    if word_found:
        print('Congrats, you won')
    else:
        print('You lost')

if __name__ == '__main__':
    start_game()
