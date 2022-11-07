#Get 2 lists
#One with all possible words
#One with all words that are still correct guesses
def get_words(difficulty, testmode = False):
    file = 'allowed_words.txt'
    if testmode:
        file = '../' + file
    with open(file, 'r') as file:
        possible_words = file.read().split('\n')

    #Each item in word_guesses is a tuple constructed like (word, number of unique letters)
    word_guesses = []
    for word in possible_words:
        word_guesses.append([word, len(set(word))])

    #filter out words depending on difficulty
    if difficulty != 'hard':
        word_guesses = remove_repeat_letters(word_guesses)
        if difficulty == 'easy':
            word_guesses = remove_words_with_jqxz(word_guesses)

    #remove unique letter count
    new_list = []
    for w in word_guesses:
        new_list.append(w[0])
    return possible_words, new_list

#remove words that don't have 5 unique letters
def remove_repeat_letters(words):
    new_list = []
    for w in words:
        if w[1] == 5:
            new_list.append(w)
    return new_list

def remove_words_with_jqxz(words):
    new_list = []
    for w in words:
        characters = set(w[0])
        filter = {'j', 'q', 'x', 'z'}
        if len(characters.intersection(filter)) == 0:
            new_list.append(w)

    return new_list