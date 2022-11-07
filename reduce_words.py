def process_guess(guess: str, possible_words):
    #split input
    guess_data = guess.split(' ')
    guess_word = guess_data[0]
    green = int(guess_data[1])
    yellow = int(guess_data[2])
    red = int(guess_data[3])
    new_list = []

    if green == 5:
        #if 5 green, you won the game
        return True, guess_word
    if red == 5:
        #if 5 red, remove all words with any of those 5 letters in them
        characters_guess_word = set(guess_word)
        for w in possible_words:
            characters_w = set(w[0])
            if len(characters_w.intersection(characters_guess_word)) == 0:
                new_list.append(w)
    else:
        characters_guess_word = []
        #get list of character of the guessed word
        for c in guess_word:
            characters_guess_word.append(c)
        for w in possible_words:
            # get list of character of the words in the possible word list
            characters_w = []
            for c in w[0]:
                characters_w.append(c)

    return False, new_list