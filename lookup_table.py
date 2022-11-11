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
'''

lookup_table = {}

def create_lookup_table():
    #get all allowed words
    with open('allowed_words.txt', 'r') as file:
        possible_words = file.read().split('\n')

    seen_words = 0 #keeping track of how many words we have seen
    with open('word_overlap.txt', 'w') as file:
        for i in range(len(possible_words)): #loop through all words
            word_new_row = possible_words[i] #get word
            list_word_new_row = [] #get char from word
            for c in word_new_row:
                list_word_new_row.append([c, False]) #boolean indicates if character is already checked
            line = ''
            for j in range(seen_words): #for all already processed words
                word_other_row = possible_words[j] #get word
                list_word_other_row = [] #get char from word
                for c in word_other_row:
                    list_word_other_row.append([c, False]) #boolean indicates if character is already checked
                #find how many letter overlap
                green = 0
                for k in range(len(word_new_row)):
                    if list_word_new_row[k][0] == list_word_other_row[k][0]:
                        green += 1
                        list_word_new_row[k][1] = True
                        list_word_other_row[k][1] = True

                #find how many yellows there are
                yellow = 0
                for k in range(len(word_new_row)):
                    if not list_word_new_row[k][1]:
                        for l in range(len(word_other_row)):
                            if k != l and not list_word_other_row[l][1] and list_word_new_row[k][0] == list_word_other_row[l][0]:
                                list_word_other_row[l][1] = True
                                yellow += 1
                                break #break for-loop j

                if line != '':
                    line += ', '
                line += str(green) + str(yellow) + str(5 - green - yellow)
            if line != '':
                line += ', '
            line += '500'
            file.write(word_new_row + ':' + line + '\n')
            seen_words += 1

def get_lookup_table():
    return lookup_table

def load_lookup_table():
    global lookup_table
    with open('word_overlap.txt', 'r') as file:
        lines = file.read().split('\n')
        for l in lines:
            split = l.split(':')
            codes = split[1].split(', ')
            numbers = [int(i) for i in codes]
            lookup_table[split[0]] = numbers
if __name__ == '__main__':
    create_lookup_table()