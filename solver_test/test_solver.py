import copy
import math
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
    for i in range(9):
        histogram[i + 1] = 0

    progress_bar = tqdm(total=len(possible_solutions), desc='Solutions checked')

    for solution in possible_solutions:
        found_solution = False
        max_guesses = False
        current_words_still_possible = copy.deepcopy(words_still_possible)
        guess_counter = 1
        guess = 'tares'
        while not (found_solution or max_guesses):
            code = lookup[guess][solution]
            if code == '500':
                histogram[guess_counter] += 1
                found_solution = True
            else:
                current_words_still_possible = solver.process_guess(guess, int(code[0]), int(code[1]), int(code[2]),
                                                                    lookup, current_words_still_possible, word_sigmoid)
                guess = solver.give_n_suggestions(1, current_words_still_possible, word_freq, guess_counter - 1, round(math.log2(len(current_words_still_possible)), 2))[0][0]
                guess_counter += 1
                if guess_counter > 8:
                    histogram[9] += 1
                    max_guesses = True
        progress_bar.update(1)
        if solution[0] == 'b':
            progress_bar.close()
            print(histogram)

            exit(0)


if __name__ == '__main__':
    run()
