def hello_dictionary():
    # no order
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
