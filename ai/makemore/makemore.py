import torch
import matplotlib.pyplot as plt

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

    # string (char) to index mapping (placing a special start/end symbol at index zero, and shifting all other by 1)
    stoi = {s: i + 1 for i, s in enumerate(chars)}
    stoi['.'] = 0  # represents start or end of a word
    print(stoi)

    # string (char) to index mapping
    itos = {i: s for s, i in stoi.items()}
    print(itos)

    dim = len(chars) + 1
    assert dim == 27  # Tensor dimension should be 27 = 26 alphabet chars + 1 special symbols for start/end

    # N is a tensor - a two-dimensional array initially filled with zeros
    N = torch.zeros((dim, dim), dtype=torch.int32)

    for w in words:
        chs = ['.'] + list(w) + ['.']
        for ch1, ch2, in zip(chs, chs[1:]):
            ix1 = stoi[ch1]
            ix2 = stoi[ch2]

            N[ix1, ix2] += 1

    plt.figure(figsize=(16, 16))
    plt.imshow(N, cmap='Blues')
    for i in range(dim):
        for j in range(dim):
            chstr = itos[i] + itos[j]
            plt.text(j, i, chstr, ha="center", va="bottom", color='gray')
            plt.text(j, i, N[i, j].item(), ha="center", va="top", color='gray')
    plt.axis('off')
    plt.show()


tensor_bigram()
