import math
import pandas as pd
from tqdm import tqdm
import copy


lookup_table = None


def create_lookup_table():
    #get all allowed words
    with open('allowed_words.txt', 'r') as file:
        possible_words = file.read().split('\n')
    global lookup_table
    col = copy.deepcopy(possible_words)
    col.append('entropy')
    lookup_table = pd.DataFrame(index=possible_words, columns=col)
    char_lookup_table = {}
    #entropy
    entropy = {}
    for w in possible_words:
        entropy[w] = {}
        for g in range(6):
            for y in range(6 - g):
                code = str(g) + str(y) + str(5 - g - y)
                entropy[w][code] = 0

    progress_bar = tqdm(total=len(possible_words), desc='Lookup table')
    for i in range(len(possible_words)):  # loop through all words
        word_new_row, list_word_new_row = get_charlist_from_word()
        char_lookup_table[word_new_row] = list_word_new_row
        for j in range(i):  # for all already processed words
            word_other_row = possible_words[j]  # get word
            list_word_other_row = copy.deepcopy(char_lookup_table[word_other_row])
            value = calculate_value(copy.deepcopy(list_word_new_row), list_word_other_row)
            entropy[word_new_row][value] += 1
            entropy[word_other_row][value] += 1
            lookup_table.loc[word_new_row][word_other_row] = value
            lookup_table.loc[word_other_row][word_new_row] = value
        lookup_table.loc[word_new_row][word_new_row] = '500'
        entropy[word_new_row]['500'] = 1
        progress_bar.update(1)
    progress_bar.close()
    progress_bar2 = tqdm(total=len(possible_words), desc='Entropy')
    for w in possible_words:
        e = 0
        for x in entropy[w].values():
            px = x/len(possible_words)
            if px > 0:
                e += px*math.log2(1/px)
        e = round(e, 2)
        lookup_table.loc[w]['entropy'] = e
        progress_bar2.update(1)
    lookup_table.to_csv('word_lookup_table.txt')
    progress_bar2.close()


#input: word like 'house'
#output: ('house', [('h', 0), ('o', 1), ('u', 2), ('s', 3), ('e', 4)])
def get_charlist_from_word(possible_words, i):
    word_new_row = possible_words[i]  # get word
    list_word_new_row = []  # get char from word
    for c in range(len(word_new_row)):
        list_word_new_row.append((word_new_row[c], c))  # c indicates position in word
    return word_new_row, list_word_new_row


#input: 2 words
#output: amount of greens, yellows, and reds
def calculate_value(copy_word_new_row, list_word_other_row):
    green = 0
    yellow = 0
    while len(copy_word_new_row) > 0:  # while still char needs to be checked
        c1, pos1 = copy_word_new_row.pop(0)  # get first char
        # define a few variables
        lowest_pos = 100
        c3 = ''
        for c2, pos2 in list_word_other_row:  # for every char still in list_word_other_row
            if c1 == c2 and pos1 == pos2:  # check for greens
                green += 1
                list_word_other_row.remove((c2, pos2))
                lowest_pos = 100  # reset value in case we id found a yellow
                break
            elif c1 == c2:  # check for yellows
                lowest_pos = pos2
                c3 = c2
        if lowest_pos != 100:  # if yellows but no green found
            yellow += 1
            list_word_other_row.remove((c3, lowest_pos))
    # adding data to both tables
    return str(green) + str(yellow) + str(5 - green - yellow)


#Because github has a file limit of 100MB, I split up the files to be accessable if someone runs my files from github
def split_lookup_table():
    global lookup_table
    print('loading lookup table')
    load_lookup_table(False)
    progress_bar = tqdm(total=13, desc='Creating parts')
    for i in range(13):
        df_part = lookup_table.iloc[1000 * i:1000 * (i + 1)]
        df_part.to_csv('lookup_table_part/part' + str(i) + '.txt')
        progress_bar.update(1)
    progress_bar.close()


def get_lookup_table():
    return lookup_table


def load_lookup_table(split):
    global lookup_table
    if split:
        lookup_table = pd.read_csv('lookup_table_part/part1.txt', index_col=[0], dtype=str)
        for i in range(1, 13):
            part = pd.read_csv('lookup_table_part/part' + str(i) + '.txt', index_col=[0], dtype=str)
            pd.concat([lookup_table, part])
    else:
        lookup_table = pd.read_csv('word_lookup_table.txt', index_col=[0], dtype=str)

if __name__ == '__main__':
    #create_lookup_table()
    split_lookup_table()
