import math


def process_guess(guess, green, yellow, red, lookup, words_still_possible, word_sigmoid):
    value = str(green) + str(yellow) + str(red)
    entropy = {}
    sum_word_sigmoid = 0
    # filter out old words and fill the 'entropy buckets'
    for word1 in words_still_possible.keys():
        if lookup.loc[guess][word1] == value:
            # setup entropy dict
            entropy[word1] = dict()
            word1_sigmoid = word_sigmoid[word1]
            for g in range(6):
                for y in range(6 - g):
                    code = str(g) + str(y) + str(5 - g - y)
                    entropy[word1][code] = 0

            # loop over all already checked and accepted words
            for word2 in entropy.keys():
                if word1 != word2:
                    code = lookup.loc[word1][word2]
                    word2_sigmoid = word_sigmoid[word2]
                    # add other word sigmoid if needed
                    entropy[word1][code] += word2_sigmoid
                    entropy[word2][code] += word1_sigmoid
                else:
                    entropy[word1]['500'] = word1_sigmoid
                    sum_word_sigmoid += word1_sigmoid

    # calculate entropy
    return_dict = {}
    sum_word_sigmoid = round(sum_word_sigmoid, 5)
    for word in entropy.keys():
        e = 0
        for value in entropy[word].values():
            px = value / sum_word_sigmoid
            if 0 < px < 1:
                e += px * math.log2(1 / px)
        return_dict[word] = round(e, 2)
    return return_dict


def give_n_suggestions(n, words_still_possible, word_freq, turn, uncertainty):
    '''
    give each word still possible a score
    return n with the highest score

    inspired by 3B1B video
    score = turn * (1 - word frequency * 10000) + (current uncertainty - entropy)
    This calculation consists of 2 parts
    The first part gives a score based on how likely it is that we guess correctly this turn.
    I multiply the word frequency by the turn, such that it has a bigger influence on the score towards the end of the game
    I do 1 - word frequency instead of word frequency, because the lower the score, the better the suggestion
    Word frequency ranges from e-05 to e-11, thus I multiple by e04 to get the range form [<-;1e-5) to [<-;1)
    The second part gives a score based on how much uncertainty we expect to have if we guess incorrectly
    '''
    scores = list()  # list of tuples: (word, score, entropy, probability)
    for word, entropy in words_still_possible.items():
        score = turn * (1 - word_freq[word] * 10_000) + uncertainty - entropy
        scores.append((word, score, entropy, word_freq[word]))

    scores_sorted = sorted(scores, key=lambda x:x[1], reverse=False)
    max_prob = 0.0
    for key, item in word_freq.items():
        if key in words_still_possible.keys():
            max_prob += item
    return_list = []
    for i in range(min(n, len(scores_sorted))):
        word, score, entropy, freq = scores_sorted[i]
        probability = 100*freq/max_prob
        return_list.append((word, round(entropy, 2), round(probability, 1)))
    return return_list