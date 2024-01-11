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


hello_dictionary()
