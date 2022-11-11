'''
Create a 2D array like this:
house [house] [pilot] [stare]
pilot [house] [pilot] [stare]
stare [house] [pilot] [stare]

Where the brackets indicate the overlapping letters between the first word in the row and the word in between the brackets
first digit: amount of greens
second digit: amount of yellows
third digit: amount of reds

such that it looks like:
house 500 014 113
pilot 014 500 014
stare 113 014 500

which is stored like
house:500, 014, 113
pilot:014, 500, 014
stare:113, 014, 500
'''

lookup_table = {}

def create_lookup_table():
    #get all allowed words
    with open('allowed_words.txt', 'r') as file:
        possible_words = file.read().split('\n')

    global lookup_table
    lookup_table.clear()
    for i in range(len(possible_words)):  # loop through all words
        word_new_row = possible_words[i]  # get word
        list_word_new_row = []  # get char from word
        lookup_table[word_new_row] = []
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
            value = str(green) + str(yellow) + str(5 - green - yellow)
            lookup_table[word_new_row].append(value)
            lookup_table[word_other_row].append(value)
        lookup_table[word_new_row].append('500')

    with open('word_overlap.txt', 'w') as file:
        line = ''
        for x in lookup_table:
            line += x + ':'
            for i in range(len(lookup_table[x]) - 1):
                line += lookup_table[x][i] + ', '
            line += lookup_table[x][-1]
        file.write(line)

def get_lookup_table():
    return lookup_table


def load_lookup_table():
    global lookup_table
    lookup_table.clear()
    with open('word_overlap.txt', 'r') as file:
        lines = file.read().split('\n')
        for l in lines:
            split = l.split(':')
            codes = split[1].split(', ')
            numbers = [int(i) for i in codes]
            lookup_table[split[0]] = numbers


if __name__ == '__main__':
    create_lookup_table()
