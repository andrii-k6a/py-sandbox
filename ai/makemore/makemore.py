import torch

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


def tensor_bigram():
    # join all words into a single string, then keep only the unique chars of the string in alphabetical order
    chars = sorted(list(set(''.join(words))))

    # string (char) to index mapping
    stoi = {s: i for i, s in enumerate(chars)}
    stoi['<S>'] = 26
    stoi['<E>'] = 27
    print(stoi)

    dim = len(chars) + 2
    assert dim == 28 # Tensor dimension should be 28 = 26 alphabet chars + 2 special start/end symbols

    # N is a tensor - a two-dimensional array initially filled with zeros
    N = torch.zeros((dim, dim), dtype=torch.int32)

    for w in words:
        chs = ['<S>'] + list(w) + ['<E>']
        for ch1, ch2, in zip(chs, chs[1:]):
            ix1 = stoi[ch1]
            ix2 = stoi[ch2]

            N[ix1, ix2] += 1

    print(N)


tensor_bigram()
