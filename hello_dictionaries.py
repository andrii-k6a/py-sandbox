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
    empty['some key'] = 333
    print(empty)


