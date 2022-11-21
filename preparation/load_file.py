import pandas as pd


def load_words(difficulty):
    with open('preparation/words_' + difficulty + '.txt', 'r') as file:
        lines = file.read().split('\n')
    return_dict = {}
    for item in lines:
        if ':' in item:
            split = item.split(': ')
            return_dict[split[0]] = float(split[1])
    return return_dict


def load_lookup_table(split):
    if split:
        lookup_table = pd.read_csv('lookup_table_part/part1.txt', index_col=[0], dtype=str)
        for i in range(1, 13):
            part = pd.read_csv('lookup_table_part/part' + str(i) + '.txt', index_col=[0], dtype=str)
            pd.concat([lookup_table, part])
    else:
        lookup_table = pd.read_csv('preparation/word_lookup_table.txt', index_col=[0], dtype=str)
    return lookup_table
