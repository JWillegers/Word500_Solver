import pandas as pd
from tqdm import tqdm
import copy


lookup_table = None


def create_lookup_table():
    #get all allowed words
    with open('allowed_words.txt', 'r') as file:
        possible_words = file.read().split('\n')
    global lookup_table
    lookup_table = pd.DataFrame(index=possible_words, columns=possible_words)
    char_lookup_table = {}
    progress_bar = tqdm(total=len(possible_words), desc='Words done')
    for i in range(len(possible_words)):  # loop through all words
        word_new_row = possible_words[i]  # get word
        list_word_new_row = []  # get char from word
        for c in range(len(word_new_row)):
            list_word_new_row.append((word_new_row[c], c))  # c indicates position in word
        char_lookup_table[word_new_row] = list_word_new_row
        for j in range(i):  # for all already processed words
            word_other_row = possible_words[j]  # get word
            list_word_other_row = copy.deepcopy(char_lookup_table[word_other_row])
            copy_word_new_row = copy.deepcopy(list_word_new_row)
            green = 0
            yellow = 0
            while len(copy_word_new_row) > 0: #while still char needs to be checked
                c1, pos1 = copy_word_new_row.pop(0) #get first char
                #define a few variables
                lowest_pos = 100
                c3 = ''
                for c2, pos2 in list_word_other_row: #for every char still in list_word_other_row
                    if c1 == c2 and pos1 == pos2: #check for greens
                        green += 1
                        list_word_other_row.remove((c2, pos2))
                        lowest_pos = 100 #reset value in case we id found a yellow
                        break
                    elif c1 == c2: #check for yellows
                        lowest_pos = pos2
                        c3 = c2
                if lowest_pos != 100: #if yellows but no green found
                    yellow += 1
                    list_word_other_row.remove((c3, lowest_pos))
            #adding data to both tables
            value = str(green) + str(yellow) + str(5 - green - yellow)
            lookup_table.loc[word_new_row][word_other_row] = value
            lookup_table.loc[word_other_row][word_new_row] = value
        lookup_table.loc[word_new_row][word_new_row] = '500'
        progress_bar.update(1)
    lookup_table.to_csv('word_lookup_table.txt')
    progress_bar.close()



def get_lookup_table():
    return lookup_table


def load_lookup_table():
    global lookup_table
    lookup_table.clear()
    with open('word_lookup_table.txt', 'r') as file:
        lines = file.read().split('\n')
        #TODO


if __name__ == '__main__':
    create_lookup_table()
