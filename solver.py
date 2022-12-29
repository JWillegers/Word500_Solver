import math

''''
OLD:
{
    house: {
        500: 1,
        401: 2
    },
    mouse: {
        500: 1,
        401: 2
    },
    rouse: {
        500: 1,
        401: 2
    }
}

NEW:
{
    house: {
        500: {
            1.0: 1
        },
        401: {
            1.0: 1
            0.01: 1
        }
    },
    mouse: {
        500: {
            1.0: 1
        },
        401: {
            1.0: 1
            0.01: 1
        }
    },
    rouse: {
        500: {
            0.01: 1
        },
        401: {
            1.0: 2
        }
    }
}
'''


def process_guess(guess, green, yellow, red, lookup, words_still_possible, word_sigmoid):
    value = str(green) + str(yellow) + str(red)
    entropy = {}
    # filter out old words and fill the 'entropy buckets'
    for word1 in words_still_possible.keys():
        if lookup.loc[guess][word1] == value:
            # setup entropy dict
            entropy[word1] = dict()
            word1_sigmoid = word_sigmoid[word1]
            for g in range(6):
                for y in range(6 - g):
                    code = str(g) + str(y) + str(5 - g - y)
                    entropy[word1][code] = dict()

            # loop over all already checked and accepted words
            for word2 in entropy.keys():
                if word1 != word2:
                    code = lookup.loc[word1][word2]
                    word2_sigmoid = word_sigmoid[word2]
                    # add other word sigmoid if needed
                    if word2_sigmoid not in entropy[word1][code].keys():
                        entropy[word1][code][word2_sigmoid] = 1
                    else:
                        entropy[word1][code][word2_sigmoid] += 1

                    if word1_sigmoid not in entropy[word2][code].keys():
                        entropy[word2][code][word1_sigmoid] = 1
                    else:
                        entropy[word2][code][word1_sigmoid] += 1
                else:
                    entropy[word1]['500'][word1_sigmoid] = 1

    # sum_word_sigmoid for words in words still possible
    sum_word_sigmoid = 0
    for w in words_still_possible.keys():
        sum_word_sigmoid += word_sigmoid[w]

    # calculate entropy
    return_dict = {}
    for word in entropy.keys():
        e = 0
        for code in entropy[word].values():
            for key, value in code.items():
                px = key / sum_word_sigmoid
                if px > 0:
                    e += value * px * math.log2(1 / px)
        return_dict[word] = round(e, 2)
    return return_dict
