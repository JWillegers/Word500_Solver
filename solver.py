import reduce_words


def process_guess(word, green, yellow, red, words_still_possible):
    guess = word + ' ' + str(green) + ' ' + str(yellow) + ' ' + str(red)
    wordfound, words_still_possible = reduce_words.process_guess(guess, words_still_possible)
    get_recommendations()
    return words_still_possible


def get_recommendations():
    global words_still_possible
    global allowed_words
    global words_entropy
    words_entropy.clear()
    ''' 
    Entropy = E[Information] = sum p(x)*Information, all x = sum p(x)*log2(1/p(x)), all x
    where Information=log2(1/p(x))
    where p(x) is the p(x) is the change that [green, yellow, red] occurs
        p(x)=len(reduced_words_still_possible)/len(current_words_still_possible)
    '''
