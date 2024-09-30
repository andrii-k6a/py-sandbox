import torch
import matplotlib.pyplot as plt

# FIXME: names.txt contains duplicate names
words = open('names.txt', 'r').read().splitlines()

# join all words into a single string, then keep only the unique chars of the string in alphabetical order
chars = sorted(list(set(''.join(words))))

# string (char) to index mapping (placing a special start/end symbol at index zero, and shifting all other by 1)
stoi = {s: i + 1 for i, s in enumerate(chars)}
stoi['.'] = 0  # represents start or end of a word
print(stoi)

# index to string (char) mapping
itos = {i: s for s, i in stoi.items()}
print(itos)

dim = len(chars) + 1
assert dim == 27  # Tensor dimension should be 27 = 26 alphabet chars + 1 special symbols for start/end

# N is a tensor - a two-dimensional array initially filled with zeros
N = torch.zeros((dim, dim), dtype=torch.int32)

# fill the tensor
for w in words:
    # add the special symbol at the start and end of the word
    chs = ['.'] + list(w) + ['.']

    # example: w = emma  ->  chs = .emma.  ->  ch1, ch2: 1) .,e 2) e,m 3) m,m 4) m,a 5) a,.
    for ch1, ch2, in zip(chs, chs[1:]):
        # encode char to index
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]

        # increase counter by index
        N[ix1, ix2] += 1

# visualize the tensor
plt.figure(figsize=(16, 16))
plt.imshow(N, cmap='Blues')
for i in range(dim):
    for j in range(dim):
        chstr = itos[i] + itos[j]
        plt.text(j, i, chstr, ha="center", va="bottom", color='gray')
        plt.text(j, i, N[i, j].item(), ha="center", va="top", color='gray')
plt.axis('off')
plt.show()

# bigram names generator
g = torch.Generator().manual_seed(2147483647)
names = []

# generate N names
for i in range(10):

    # zero row in tensor is probability distribution of letters a name starts with
    ix = 0
    name = ''

    while True:
        # get probability distribution
        p = N[ix].float()

        # normalize probability distribution
        p = p / p.sum()

        # random index of the probability distribution array
        ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()

        # zero column in tensor is probability distribution of letters a name ends with
        if ix == 0:
            break

        # add next char to a name
        name += itos[ix]

    names.append(name)

print(names)
