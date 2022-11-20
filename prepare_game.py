import lookup_table
from tqdm import tqdm
'''
OLD TUI METHONDS
'''
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
        word_guesses = old_remove_repeat_letters(word_guesses)
        if difficulty == 'easy':
            word_guesses = old_remove_words_with_jqxz(word_guesses)

    #remove unique letter count
    new_list = []
    for w in word_guesses:
        new_list.append(w[0])
    return possible_words, new_list


#remove words that don't have 5 unique letters
def old_remove_repeat_letters(words):
    new_list = []
    for w in words:
        if w[1] == 5:
            new_list.append(w)
    return new_list


def old_remove_words_with_jqxz(words):
    filter = {'j', 'q', 'x', 'z'}
    new_list = []
    for w in words:
        characters = set(w[0])
        if len(characters.intersection(filter)) == 0:
            new_list.append(w)

    return new_list

'''
NEW LOOKUP TABLE METHODS
'''


def get_table(difficulty, split_mode):
    with open('allowed_words.txt', 'r') as file:
        allowed_words = file.read().split('\n')

    lookup_table.load_lookup_table(split_mode)
    lt = lookup_table.get_lookup_table()
    print('hi')
    if difficulty != 'hard':
        lt = remove_repeat_letters(lt)
        if difficulty == 'easy':
            lt = remove_words_with_jqxz(lt)
    print(lt)
    return allowed_words, lt


def remove_repeat_letters(lt):
    pb = tqdm(total=len(lt.index), desc='Remove repeat letters')
    for i, row in lt.iterrows():
        if len(set(i)) != 5:
            lt.drop(i, inplace=True, axis=0)
            lt.drop(i, inplace=True, axis=1)
        pb.update(1)
    pb.close()
    return lt


def remove_words_with_jqxz(lt):
    pb = tqdm(total=len(lt.index), desc='Remove JQXZ')
    filter = {'j', 'q', 'x', 'z'}
    for i, row in lt.iterrows():
        if set(i).intersection(filter) != 0:
            lt.drop(i, inplace=True, axis=0)
            lt.drop(i, inplace=True, axis=1)
        pb.update(1)
    pb.close()
    return lt
