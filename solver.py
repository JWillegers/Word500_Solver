import math


def process_guess(guess, green, yellow, red, lookup, words_still_possible):
    value = str(green) + str(yellow) + str(red)
    entropy = {}
    # filter out old words and fill the 'entropy buckets'
    print('========== ' + guess + ' ==========')
    for word1 in words_still_possible.keys():
        if lookup.loc[guess][word1] == value:
            print(word1)
            #setup entropy dict
            entropy[word1] = {}
            for g in range(6):
                for y in range(6 - g):
                    code = str(g) + str(y) + str(5 - g - y)
                    entropy[word1][code] = 0

            #loop over all already checked and accepted words
            for word2 in entropy.keys():
                if word1 != word2:
                    code = lookup.loc[word1][word2]
                    entropy[word1][code] += 1
                    entropy[word2][code] += 1
                else:
                    entropy[word1]['500'] += 1

    # calculate entropy
    return_dict = {}
    for w in entropy.keys():
        e = 0
        for x in entropy[w].values():
            px = x / len(entropy)
            if px > 0:
                e += px * math.log2(1 / px)
        return_dict[w] = round(e, 2)
    return return_dict
