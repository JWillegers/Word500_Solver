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
    elif red == 5:
        #if 5 red, remove all words with any of those 5 letters in them
        characters_guess_word = set(guess_word)

        for w in possible_words:
            characters_w = set(w)
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
            for c in w:
                characters_w.append(c)
            if match_words(characters_guess_word, characters_w, green, yellow):
                new_list.append(w)

    return False, new_list

def match_words(characters_guess_word, characters_w, green ,yellow):
    list_gw = []
    list_w = []
    for w in characters_w:
        list_w.append([w, False])  # boolean indicates if character is match to a character in characters_guess_word
    for w in characters_guess_word:
        list_gw.append([w, False])  # boolean indicates if character is match to a character in characters_guess_word


    #check how many greens there are
    count_green = 0
    for i in range(len(characters_guess_word)):
        if characters_guess_word[i] == list_w[i][0]:
            count_green += 1
            list_gw[i][1] = True
            list_w[i][1] = True

    if green != count_green:
        return False

    #check how many yellows there are
    count_yellow = 0
    for i in range(len(characters_guess_word)):
        if not list_gw[i][1]:
            for j in range(len(list_w)):
                if i != j and not list_w[j][1]: #if index different and letter not marked checked
                    if list_gw[i][0] == list_w[j][0]: #if letters are the same
                        list_w[j][1] = True
                        count_yellow += 1
                        break #break for-loop j

    return count_yellow == yellow

