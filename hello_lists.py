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


def concatenating_lists():
    a = [1, 2, 3]
    b = [99, 88, 77]
    c = a + b
    print(a)
    print(b)
    print('Concatenating result', c)


def slice_list():
    l = [99, 11, 88, 77, 42]
    print("Initial list:", l)

    # work the same way as for strings
    print('l[1:3] -', l[1:3])
    print('l[2:4] -', l[2:4])
    print('l[1:] -', l[1:])
    print('l[:2] -', l[:2])
    print('l[1:333] -', l[1:333])
    print('l[:333] -', l[:333])
    print('l[333:] -', l[333:])
    print('l[333:333] -', l[333:333])
    print('l[:] -', l[:])


def start_stop_step_slicing():
    nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]
    print(nums)

    # name[start_including : stop_not_including : step]
    print('nums[1:7:2] -', nums[1:7:2])
    print('nums[::2] -', nums[::2])


def list_exploration():
    just_list = list()
    # <class 'list'>
    print(type(just_list))
    print(dir(just_list))


def building_list():
    stuff = list()
    print(stuff)

    stuff.append('phone')
    stuff.append(42)
    print(stuff)

    stuff.append('umbrella')
    print(stuff)


def check_if_list_contains():
    values = ['dog', 4, 31, 5.0, 'banana', [1, 0, 1]]
    print('Initial values:', values)

    if 'banana' in values:
        print('There is a banana')

    if 'cat' not in values:
        print('There is no cats')

    if [1, 0, 1] in values:
        print('Huh, there is a list in a list...')


def sort_lists():
    nums = [7, 1, -3, 15, 23, 22, 15]
    print('Initial:', nums)
    nums.sort()
    print('Sorted:', nums)

    names = ['Mary', 'Andy', 'Susan', 'Max']
    print('Initial:', names)
    names.sort()
    print('Sorted:', names)

    # Cannot sort mixed list...
    # TypeError: '<' not supported between instances of 'int' and 'str'
    mixed = ['Mary', 2, 'Andy', 'Max', 3.5, 'Susan', -1]
    print('Initial:', mixed)
    # mixed.sort()


def functions_for_lists():
    nums = [7, 3, 7, 1, -5, 0]
    print('Initial:', nums)
    print('len', len(nums))
    print('max', max(nums))
    print('min', min(nums))
    print('sum', sum(nums))
    print('sum/len', sum(nums) / len(nums))


def split_string_to_list():
    # intentionally added extra spaces
    text = 'Welcome to    my world!'
    words = text.split()
    print(words)
    print('Number of words', len(words))
    print('First word -', words[0])

    for word in words:
        print(word.upper(), end=", ")
    print('\nDone')


def split_string_to_list_with_semicolon():
    text = 'Welcome;to;my;world'
    print('Split by space', text.split())
    print('Split by semicolon', text.split(';'))


