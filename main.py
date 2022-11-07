import prepare_game
import reduce_words


def start_game():
    difficulty = input('Which difficult do you want to play on? (easy/medium/hard)')
    possible_words, possible_words = prepare_game.get_words(difficulty)
    word_found = False
    turn_counter = 1
    while not word_found and turn_counter <= 8:
        guess = input('What did you guess? answer format: word [space] amount green [space] amount yellow [space] amount red')
        word_found, possible_words = reduce_words.process_guess(guess, possible_words)
        turn_counter += 1
    if word_found:
        print('Congrats, you won')
    else:
        print('You lost')

if __name__ == '__main__':
    start_game()
