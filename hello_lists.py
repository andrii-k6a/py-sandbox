def hello_list():
    numbers = [4, 3, 7, -1]
    for i in numbers:
        print(i)
    print('Done')


def get_by_index():
    numbers = [4, 3, 7, -1]

    # IndexError: list index out of range
    # print(numbers[10])

    print('Zero element is', numbers[0])


def update_list():
    numbers = [9, 8, 7, 6, 5]
    print('Initial list:', numbers)
    numbers[1] = 42
    print('Updated list:', numbers)

    hello = 'hello'
    # Strings are immutable - TypeError: 'str' object does not support item assignment
    # hello[1] = 'q'
    print(hello)


def list_size():
    items = ['Alex', 'Glen', 15, 5.0, [1, 1, 0]]
    print('Items size:', len(items))


def hello_range():
    # Range and other functional-style methods, such as map, reduce, and filter, return iterators in Python 3.
    # In Python 2 they returned lists.
    positive = range(5)
    print(list(positive))
    print('The len is', len(positive))

    # empty iterator
    negative = range(-5)
    print('This is empty list - ', list(negative))


def another_iteration_example():
    names = ['Steve', 'Maria', 'Kristi']

    for name in names:
        print('Hello', name)

    for i in range(len(names)):
        name = names[i]
        print('Bye', name)


