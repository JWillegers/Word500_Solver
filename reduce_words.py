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
            for c in w:
                characters_w.append(c)
            if yellow == 0: #only greens
                #why not combine the 2 ifs? because I don't want to be difficult with the else
                if match_greens(characters_guess_word, characters_w) == green:
                    new_list.append(w)
            elif green == 0: #only yellow
                if match_yellows(characters_guess_word, characters_w) == yellow:
                    new_list.append(w)
            else:
                test = True

    return False, new_list

#for word a and word b, count how often a[i] == b[i], where a[i] and b[i] are char at index i of each word
def match_greens(characters_guess_word, characters_w):
    count = 0
    for i in range(len(characters_guess_word)):
        if characters_guess_word[i] == characters_w[i]:
            count += 1
    return count

#
def match_yellows(characters_guess_word, characters_w):
    count = 0
    list_w = []
    for w in characters_w:
        list_w.append([w, False]) #boolean indicates if character is match to a character in characters_guess_word
    #if any letters are at the same position at both words, that letter will be marked checked (True)
    #example: beans and rains -> n, s will be marked checked, but a will not
    for i in range(len(characters_guess_word)):
        if characters_guess_word[i] == list_w[i][0]:
            list_w[i][1] = True
    for i in range(len(characters_guess_word)):
        for j in range(len(list_w)):
            if i != j and not list_w[j][1]: #if index different and letter not marked checked
                if characters_guess_word[i] == list_w[j][0]: #if letters are the same
                    list_w[j][1] = True
                    count += 1
                    break #break for-loop j
    return count
