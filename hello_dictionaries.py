def hello_dictionary():
    # no order
    # As of Python 3.7, dicts retaining insertion order is guaranteed
    bag = dict()
    print(type(bag))

    bag['phone'] = 1
    bag['candy'] = 42
    bag['book'] = 3
    print(bag)
    print(bag['candy'])

    bag['candy'] = bag['candy'] - 10
    print(bag['candy'])
    print(bag)


def dictionary_declaration():
    person = {'name': 'Cindy', 'age': 25, 'address': {'city': 'NY', 'country': 'US'}}
    print('Person type:', type(person))
    print(person)

    # {} is the same as dict()
    empty = {}
    print('Empty dictionary type:', type(empty))
    print(empty)
    # if try to get value by non-existent key -  KeyError: 'hello'
    # print(empty['hello'])
    empty['some key'] = 333
    print(empty)


def names_histogram(names: list):
    name_to_counter = dict()
    for name in names:
        if name in name_to_counter:
            name_to_counter[name] = name_to_counter[name] + 1
        else:
            name_to_counter[name] = 1

        # another way with a default value if key does not exist
        # name_to_counter[name] = name_to_counter.get(name, 0) + 1

    print(name_to_counter)


# names_histogram(['Elaine', 'Ben', 'Elaine', 'Max', 'Ben', 'Cindy', 'Carlos', 'Elaine', 'Ben', 'Ben'])


def count_words():
    poem_file = open('resources/poem.txt')
    word_to_counter = dict()

    for line in poem_file:
        words = line.split()
        for word in words:
            if word.lower() == 'a' or word.lower() == 'an' or word.lower() == 'the':
                continue

            if word.endswith('.') or word.endswith(','):
                word = word[:len(word) - 1]

            word_to_counter[word] = word_to_counter.get(word, 0) + 1

    print(word_to_counter)


def iterate_over_dict():
    # If dictionary contains duplicates, it overrides with the latest value
    histogram = {'hello': 3, 'world': 7, 'from': 5, 'dictionary': 13, 'hello': 35}

    # k - key
    for k in histogram:
        print('*****')
        print('Key:', k)
        print('Value:', histogram[k])
    print('*** Done ***')


def keys_and_values():
    data = {'abc': 11, 'bbb': 2, 'ced': 33, 'def': 4}
    print(data)

    print('To list:', type(list(data)), list(data))
    # use list() to convert types below to list, like 'list(data.keys())'
    print('Keys:', type(data.keys()), data.keys())
    print('Values:', type(data.values()), data.values())
    print('Items:', type(data.items()), data.items())


def key_value_iteration():
    data = {'abc': 333, 'bbb': 22, 'c': 3, 'd': 444}
    # iteration with two iteration variables
    for k, v in data.items():
        print('Key:', k, 'Value:', v)


def most_frequent_word():
    poem_file = open('resources/poem.txt')
    word_to_counter = dict()

    for line in poem_file:
        words = line.split()
        for word in words:
            word_to_counter[word] = word_to_counter.get(word, 0) + 1

    big_word = None
    big_count = None
    for word, counter in word_to_counter.items():
        if big_count is None or counter > big_count:
            big_word = word
            big_count = counter

    print(big_word, big_count)


def sorting_items_in_dict():
    d = {'c': 10, 'a': 333, 'd': 99, 'b': 0}
    print(d.items())

    # since keys are unique in dict, tuples in dict are sorted by keys no matter what value is
    sorted_items = sorted(d.items())
    print(sorted_items)


def iterate_over_sorted_dict():
    d = {'c': 10, 'a': 333, 'd': 99, 'b': 0}
    print(d)

    for k, v in sorted(d.items()):
        print(k, v)
    print('Done')


def sort_dict_by_value():
    d = {'c': 10, 'a': 333, 'd': 99, 'b': 0, 'e': 333, 'f': 1000, 'g': 100}
    print(d)

    tuples_list = list()
    for k, v in d.items():
        tuples_list.append((v, k))
    print(tuples_list)

    r1 = sorted(tuples_list)
    print('Sorted -', r1)
    r2 = sorted(tuples_list, reverse=True)
    print('Reverse -', r2)



