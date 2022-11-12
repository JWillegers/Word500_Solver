'''
entropy_table.txt format
word:[005: [words]], [014: [words]], etc

lookup_table.txt format
word:(other_word, code), (word3, code), etc
'''

entropy_table = {}
lookup_table = {}


def create_lookup_and_entropy_table():
    #get all allowed words
    with open('allowed_words.txt', 'r') as file:
        possible_words = file.read().split('\n')

    global lookup_table
    lookup_table.clear()
    global entropy_table
    entropy_table.clear()
    for i in range(len(possible_words)):  # loop through all words
        word_new_row = possible_words[i]  # get word
        list_word_new_row = []  # get char from word
        lookup_table[word_new_row] = {}
        entropy_table[word_new_row] = {}
        for green in range(6):
            for yellow in range(6-green):
                entropy_table[word_new_row][str(green) + str(yellow) + str(5 - green - yellow)] = []

        for c in word_new_row:
            list_word_new_row.append([c, False])  # boolean indicates if character is already checked
        for j in range(i):  # for all already processed words
            word_other_row = possible_words[j]  # get word
            list_word_other_row = []  # get char from word
            for c in word_other_row:
                list_word_other_row.append([c, False])  # boolean indicates if character is already checked
            # find how many letter overlap
            green = 0
            for k in range(len(word_new_row)):
                if list_word_new_row[k][0] == list_word_other_row[k][0]:
                    green += 1
                    list_word_new_row[k][1] = True
                    list_word_other_row[k][1] = True

            # find how many yellows there are
            yellow = 0
            for k in range(len(word_new_row)):
                if not list_word_new_row[k][1]:
                    for l in range(len(word_other_row)):
                        if k != l and not list_word_other_row[l][1] and \
                                list_word_new_row[k][0] == list_word_other_row[l][0]:
                            list_word_other_row[l][1] = True
                            yellow += 1
                            break  # break for-loop j

            #adding data to both tables
            value = str(green) + str(yellow) + str(5 - green - yellow)
            entropy_table[word_new_row][value].append(word_other_row)
            entropy_table[word_other_row][value].append(word_new_row)
            lookup_table[word_new_row][word_other_row] = value
            lookup_table[word_other_row][word_new_row] = value

        entropy_table[word_new_row]['500'].append(word_new_row)
        lookup_table[word_new_row][word_new_row] = '500'

    with open('word_entropy_table.txt', 'w') as file:
        for word in entropy_table:
            line = word + ':' #line = 'word:'
            for code in entropy_table[word]:
                line += '[' + code + ': ' #line looks like: 'word:(all previous rounds)[code: '
                for w in entropy_table[word][code]:
                    line += w + ', ' #line looks like: 'word:[code: trees, words,'
                line = line[:-2] #delete last comma and space
                line += '], ' #line looks like: 'word:[code: trees, words],'
            line = line[:-2]  # delete last comma and space
            file.write(line + '\n')

    with open('word_lookup_table.txt', 'w') as file:
        for word in lookup_table:
            line = word + ':'  # line = 'word:'
            for other_word in lookup_table[word]:
                line += '(' + other_word + ', ' + lookup_table[word][other_word] + '), '
            line = line[:-2]  # delete last comma and space
            file.write(line + '\n')


def get_entropy_table():
    return entropy_table


def get_lookup_table():
    return lookup_table


def load_entropy_table():
    global entropy_table
    entropy_table.clear()
    with open('word_entropy_table.txt', 'r') as file:
        lines = file.read().split('\n')
        #TODO


if __name__ == '__main__':
    create_lookup_and_entropy_table()
