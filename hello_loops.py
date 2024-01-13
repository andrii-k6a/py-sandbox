def simple_for_loop():
    print('Counting from 5 to 1')
    for number in [5, 4, 3, 2, 1]:
        print('Number -', number)
    print('Done')


def iterate_over_list():
    names = ['Charles', 'Andrii', 'Mary']
    print('Iterating over list:', names)
    for name in names:
        print('Hello', name)
    print('Done')


def smallest_number(numbers: list):
    smallest = None
    print(smallest)
    print(type(smallest))

    for number in numbers:
        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number

    return smallest

# print(smallest_number([1, 4, -4, 6, 3, -8, 3, 19, 1]))


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


def loop_scope():
    for i in [1, 2, 3]:
        print(i)
        for j in ['a', 'b']:
            print(j)

    for k in [333, 444]:
        # i and j are accessible here
        print(k, i, j)



