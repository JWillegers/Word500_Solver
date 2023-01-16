import copy
import json
import solver
import first_guess
import lookup_table
import frequencies


def run(word):
    original_words_still_possible = first_guess.load_words('hard', True)
    original_words_still_possible = dict(
        sorted(original_words_still_possible.items(), key=lambda item: item[1], reverse=True))  # sort by entropy decreasing
    lookup = lookup_table.load_lookup_table(True)
    word_sigmoid = frequencies.get_sigmoid(True)
    assert(word in original_words_still_possible.keys())
    save = dict()
    for green in range(6):
        for yellow in range(6 - green):
            red = 5 - green - yellow
            wsp = solver.process_guess(word, green, yellow, red, lookup, copy.deepcopy(original_words_still_possible), word_sigmoid)
            code = str(green) + str(yellow) + str(red)
            save[code] = wsp
    with open('second_guess/' + word + '.txt', 'w') as file:
        json.dump(save, file, indent=4)


if __name__ == '__main__':
    # argument 5-letter word which is in allowed words
    run('tares')
