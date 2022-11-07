import prepare_game


def start_game():
    difficulty = input('Which difficult do you want to play on? (easy/medium/hard)')
    ossible_words, word_guesses = prepare_game.get_words(difficulty)

if __name__ == '__main__':
    start_game()
