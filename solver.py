'''
Implementation of idea 2, algorithm 3 in 'Data & The Solver.docx'
'''
import math


def process_guess(word, green, yellow, red, lookup_table):
    value = str(green) + str(yellow) + str(red)
    lookup_table = reduce_dataframe(word, value, lookup_table)
    lookup_table = calculate_entropy(lookup_table)
    return lookup_table


def reduce_dataframe(word, value, df):
    for column in df:
        if column != word and column != 'entropy' \
                and value != df.loc[word][column]:
            df.drop(column, inplace=True, axis=1)
            df.drop(column, inplace=True, axis=0)
    if value != df.loc[word][word]:
        df.drop(word, inplace=True, axis=1)
        df.drop(word, inplace=True, axis=0)
    return df


def calculate_entropy(lookup_table):
    for i, row in lookup_table.iterrows():
        entropy = {}
        for col in lookup_table:
            if col != 'entropy':
                value = lookup_table.loc[i][col]
                if value in entropy:
                    entropy[value] += 1
                else:
                    entropy[value] = 1
        e = 0
        for v in entropy.values():
            px = v/len(lookup_table.index)
            if px > 0:
                e += px*math.log2(1/px)
        e = round(e, 2)
        lookup_table.at[i, 'entropy'] = e
    return lookup_table
