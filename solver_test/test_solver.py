import copy
import math
import json
import solver
from tqdm import tqdm
from preparation import first_guess
from preparation import lookup_table
from preparation import frequencies


def run():
    with open('possible_solution.txt', 'r') as file:
        possible_solutions = file.read().split('\n')

    words_still_possible = first_guess.load_words('hard', True)
    words_still_possible = dict(
        sorted(words_still_possible.items(), key=lambda item: item[1], reverse=True))  # sort by entropy decreasing
    lookup = lookup_table.load_lookup_table(True)
    word_sigmoid = frequencies.get_sigmoid(other_folder=True)
    word_freq = frequencies.get_frequencies(True)

    histogram = dict()
    for i in range(20):
        histogram[i + 1] = 0

    progress_bar = tqdm(total=len(possible_solutions), desc='Solutions checked')

    start_guess = 'tares'  # starting word, make sure there is a file in preparation/second_guess called [guess].txt (e.g. 'tares_v1.txt')
    with open('../preparation/second_guess/' + start_guess + '.txt', 'r') as file:
        second_guess = json.load(file)

    for solution in possible_solutions:
        found_solution = False
        max_guesses = False
        current_words_still_possible = copy.deepcopy(words_still_possible)
        guess_counter = 1
        first_guess_bool = True
        guess = copy.deepcopy(start_guess)
        while not (found_solution or max_guesses):
            code = lookup[guess][solution]
            if code == '500':
                histogram[guess_counter] += 1
                found_solution = True
            else:
                if first_guess_bool:
                    first_guess_bool = False
                    current_words_still_possible = second_guess[code]
                else:
                    current_words_still_possible = solver.process_guess(guess, int(code[0]), int(code[1]), int(code[2]),
                                                                        lookup, current_words_still_possible, word_sigmoid)
                guess = solver.give_n_suggestions(1, current_words_still_possible, word_freq, guess_counter - 1,
                                                  round(math.log2(len(current_words_still_possible)), 2))[0][0]
                guess_counter += 1
        progress_bar.update(1)
    progress_bar.close()
    print(histogram)
    with open('results/' + start_guess + '.txt', 'w') as file:
        json.dump(histogram, file, indent=4)
    total = 0
    for key, item in histogram.items():
        total += key * item
    print('mean:', total / len(possible_solutions))


if __name__ == '__main__':
    run()
