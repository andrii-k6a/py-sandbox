# FIXME: names.txt contains duplicate names
words = open('names.txt', 'r').read().splitlines()


def print_words_info():
    print('First 10 words:', words[:10])
    print('Words len:', len(words))
    print('Word Min Len', min(len(w) for w in words))
    print('Word Max Len', max(len(w) for w in words))


# A bigram is a sequence of two consecutive elements, such as two nearby characters in a word
def simple_bigram():
    # A bigram dictionary where the key is a tuple of two characters, representing the second character following
    # the first in words, and the value is a counter of how often this occurs
    b = {}

    for w in words:

        # add two special symbols to represent the start and end of the word
        chs = ['<S>'] + list(w) + ['<E>']

        # example: w = emma  ->  chs = <S>emma<E>  ->  ch1, ch2: 1) <S>,e 2) e,m 3) m,m 4) m,a 5) a,<E>
        for ch1, ch2, in zip(chs, chs[1:]):
            bigram = (ch1, ch2)

            # increase counter by the bigram
            b[bigram] = b.get(bigram, 0) + 1

    # print the items of the bigram dictionary sorted by the value (bigram counter) in descending order
    for item in sorted(b.items(), key=lambda kv: -kv[1]):
        print(item)
