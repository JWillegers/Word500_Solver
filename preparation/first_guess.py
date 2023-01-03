from copy import deepcopy
from tqdm import tqdm
from preparation import lookup_table
import math
import frequencies


def run():
    with open('allowed_words.txt', 'r') as file:
        possible_words = file.read().split('\n')
    word_sigmoid = frequencies.get_sigmoid(same_folder=True)
    lt = lookup_table.load_lookup_table(True)

    pw_hard_dict = calculate_entropy(possible_words,  lt, word_sigmoid)
    write_to_file('hard', pw_hard_dict)

    pw_medium = medium(deepcopy(possible_words))
    pw_medium_dict = calculate_entropy(pw_medium,  lt, word_sigmoid)
    write_to_file('medium', pw_medium_dict)

    pw_easy = easy(pw_medium)
    pw_easy_dict = calculate_entropy(pw_easy, lt, word_sigmoid)
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


def calculate_entropy(possible_words, lookup, word_sigmoid):
    # setup dict
    entropy = {}
    for w in possible_words:
        entropy[w] = {}
        for g in range(6):
            for y in range(6 - g):
                code = str(g) + str(y) + str(5 - g - y)
                entropy[w][code] = 0

    # loop through all words and find the 'entropy buckets'
    loop_pb = tqdm(total=len(possible_words), desc='Loop through words')
    sum_word_sigmoid = 0
    for i in range(len(possible_words)):
        word_i = possible_words[i]
        word_i_sigmoid = word_sigmoid[word_i]
        for j in range(i):
            word_j = possible_words[j]
            word_j_sigmoid = word_sigmoid[word_j]
            value = lookup.loc[word_i][word_j]
            entropy[word_i][value] += word_j_sigmoid
            entropy[word_j][value] += word_i_sigmoid
        entropy[word_i]['500'] += word_i_sigmoid
        sum_word_sigmoid += word_i_sigmoid
        loop_pb.update(1)
    loop_pb.close()

    #calculate entropy
    return_dict = {}
    sum_word_sigmoid = round(sum_word_sigmoid, 5)
    for w in possible_words:
        e = 0
        for x in entropy[w].values():
            px = x / sum_word_sigmoid
            if 0 < px < 1:
                e += px * math.log2(1 / px)
        return_dict[w] = round(e, 2)
    return return_dict


def write_to_file(diff, pw):
    with open('words_' + diff + '.txt', 'w') as file:
        for key, value in pw.items():
            file.write(str(key) + ': ' + str(value) + '\n')


def load_words(difficulty):
    with open('preparation/words_' + difficulty + '.txt', 'r') as file:
        lines = file.read().split('\n')
    return_dict = {}
    for item in lines:
        if ':' in item:
            split = item.split(': ')
            return_dict[split[0]] = float(split[1])
    return return_dict


if __name__ == '__main__':
    run()
