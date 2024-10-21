import torch
import matplotlib.pyplot as plt

# FIXME: names.txt contains duplicate names
words = open('names.txt', 'r').read().splitlines()

# join all words into a single string, then keep only the unique chars of the string in alphabetical order
chars = sorted(list(set(''.join(words))))

# string (char) to index mapping (placing a special start/end symbol at index zero, and shifting all other by 1)
stoi = {s: i + 1 for i, s in enumerate(chars)}
stoi['.'] = 0  # represents start or end of a word

# index to string (char) mapping
itos = {i: s for s, i in stoi.items()}

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

# normalized probability distribution
P = N.float()
P /= P.sum(dim=1, keepdim=True)

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
        p = P[ix]

        # random index of the probability distribution array
        ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()

        # zero column in tensor is probability distribution of letters a name ends with
        if ix == 0:
            break

        # add next char to a name
        name += itos[ix]

    names.append(name)

print(names)

# Likelihood is the product of probabilities (Search for: Maximum Likelihood Estimation)
log_likelihood = 0.0
n = 0.0

for w in words:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2, in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        prob = P[ix1, ix2]

        # Log-likelihood simplifies computation by turning the product of probabilities into a sum, preventing numerical
        # underflow and making optimization easier while still leading to the same parameter estimates as likelihood:
        # log(a*b*c) = log(a) + log(b) + log(c)
        logprob = torch.log(prob)
        log_likelihood += logprob
        n += 1
        # print(f'{ch1}{ch2} : {prob:.4f} : {logprob:.4f}')

print(f'{log_likelihood=}')

# negative log likelihood aligns with loss function semantics - the lower value, the better
nll = -log_likelihood
print(f'{nll=}')
print(f'normalized (average instead of sum) loss = {nll / n}')
