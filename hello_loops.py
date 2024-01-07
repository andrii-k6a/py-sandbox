def even_or_odd(n: int = 5):
    print("Even or odd?")
    for i in range(n):
        if i % 2 == 0:
            print(i, "- even")
        else:
            print(i, "- odd")
    print("Done")


def from_n_to_zero(n: int = 5):
    print('Iterating from N to zero')
    while n > 0:
        print('Current number is', n)
        n = n - 1
    print('Done')


def repeater():
    while True:
        line = input('> ')
        if line.startswith('#'):
            continue
        if line == 'exit':
            break
        print(line)
    print('Goodbye!')



