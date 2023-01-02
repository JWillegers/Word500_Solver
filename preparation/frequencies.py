import json
import math
import numpy as np


def get_sigmoid():
    # word frequency -> sigmoid function (credit to 3B1B)
    with open('preparation/word_freq.json', 'r') as file:
        freq_map = json.load(file)
    words = np.array(list(freq_map.keys()))
    freqs = np.array([freq_map[w] for w in words])
    arg_sort = freqs.argsort()
    sorted_words = words[arg_sort]
    # variables that can be changed, the lower x_width and the higher rounding factor, the higher computation time is
    x_width = 50  # range of x in sigmoid function (can be from 0 to 100 or -70 to 30 or something else)
    n_common = 3000  # how far from the most common word roughly the point where about halve the words are common enough to be guesses
    round_factor = 3  # by how many decimals do we round?
    # calculations
    center = x_width * (-0.5 + n_common / len(words))
    xs = np.linspace(center - x_width / 2, center + x_width / 2, len(words))
    word_sigmoid = dict()
    for word, x in zip(sorted_words, xs):
        word_sigmoid[word] = max(round(1/(1 + np.exp(-x)), round_factor), math.pow(10, -round_factor))
    return word_sigmoid


def get_frequencies():
    with open('preparation/word_freq.json', 'r') as file:
        freq_map = json.load(file)
    return freq_map
