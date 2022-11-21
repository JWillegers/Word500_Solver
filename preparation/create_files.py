from copy import deepcopy
from tqdm import tqdm
import lookup_table
import math


def run():
    with open('allowed_words.txt', 'r') as file:
        possible_words = file.read().split('\n')
    lookup_table.load_lookup_table(False)
    lt = lookup_table.get_lookup_table()

    pw_hard_dict = calculate_entropy(possible_words,  lt)
    write_to_file('hard', pw_hard_dict)

    pw_medium = medium(deepcopy(possible_words))
    pw_medium_dict = calculate_entropy(pw_medium,  lt)
    write_to_file('medium', pw_medium_dict)

    pw_easy = easy(pw_medium)
    pw_easy_dict = calculate_entropy(pw_easy, lt)
    write_to_file('easy', pw_easy_dict)


# remove words with j,q,x,z
def easy(possible_words):
    new_pw = []
    filter = {'j', 'q', 'x', 'z'}
    for word in possible_words:
        if len(set(word).intersection(filter)) == 0:
            new_pw.append(word)
    return new_pw


# remove words with double letters
def medium(possible_words):
    new_pw = []
    for word in possible_words:
        if len(set(word)) == 5:
            new_pw.append(word)
    return new_pw


def calculate_entropy(possible_words, lookup):
    # setup dict
    entropy = {}
    for w in possible_words:
        entropy[w] = {}
        for g in range(6):
            for y in range(6 - g):
                code = str(g) + str(y) + str(5 - g - y)
                entropy[w][code] = 0

    # loop through all words
    loop_pb = tqdm(total=len(possible_words), desc='Loop through words')
    for i in range(len(possible_words)):
        word_i = possible_words[i]
        for j in range(i):
            word_j = possible_words[j]
            value = lookup.loc[word_i][word_j]
            entropy[word_i][value] += 1
            entropy[word_j][value] += 1
        entropy[word_i]['500'] += 1
        loop_pb.update(1)
    loop_pb.close()

    #calculate entropy
    return_dict = {}
    for w in possible_words:
        e = 0
        for x in entropy[w].values():
            px = x / len(possible_words)
            if px > 0:
                e += px * math.log2(1 / px)
        return_dict[w] = round(e, 2)
    return return_dict


def write_to_file(diff, pw):
    with open('words_' + diff + '.txt', 'w') as file:
        for key, value in pw.items():
            file.write(str(key) + ': ' + str(value) + '\n')


if __name__ == '__main__':
    run()
