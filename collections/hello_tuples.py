def simple_tuple():
    # tuple declaration - ()
    # Tuples are another kind of sequence that functions much like a list
    t = ('a1', 'b2', 'c3')

    print(t)
    print(type(t))
    print(dir(t))
    print(t[1])
    print(len(t))
    print(max(t))


def single_tuple():
    t1 = ('hello')   # string
    t2 = ('world',)  # tuple with a single value
    print(type(t1), t1)
    print(type(t2), t2)


def tuples_are_immutable():
    t = (5, 4, 3)
    print(t)

    # TypeError: 'tuple' object does not support item assignment
    # t[0] = 42


def tuple_on_the_left_hand_side_of_assignment():
    # like two assignments statement
    (name, age) = ('Fred', 42)
    print(name, age)
    print(type(name), type(age))

    a, b, c = (11, 333, 7)
    print(a, b, c)
    print(type(a), type(b), type(c))

    # the amount of vars and values has to match
    # q, w = (1, 2, 3, 4)
    # s, d, f = (1, 2)


def tuple_in_dict():
    d = dict()
    d['a'] = 10
    d['b'] = 42
    print(d)

    for k, v in d.items():
        print(k, v)

    # items in dictionary are tuples
    print(list(d.items()))
    i = list(d.items())[1]
    print(type(i))


def tuples_are_comparable():
    t1 = (10, -1, -5, 0)
    t2 = (9, 42, 333, 68, 55, 100)
    print(t1, t2)

    # if the first element is equal, Python goes on to the next element, and so on,
    # until it finds elements that differ
    if t1 > t2:
        print(t1, 'bigger than', t2)

    if (1, 2, 3, -100) > (1, 2, 3):
        print('Longer wins if all items before are equal')

    if ('Max', 'Adam') < ('Max', 'Nina'):
        print('(Max, Adam) < (Max, Nina) is True, because N is greater than A')

    print('Done')


def sorting_list_of_tuples():
    list_of_tuples = [('c', 10), ('a', 333), ('d', 99), ('b', 0)]
    print(list_of_tuples)

    # does not sort the source list, but provides a new sorted one
    sorted_list_of_tuples = sorted(list_of_tuples)
    print(list_of_tuples)
    print(sorted_list_of_tuples)


def tuple_concatenation():
    a = (1, 2, 3)
    b = (4, 5)
    c = ('c', 'b', 'a')
    print(a + b + c)


def nested_tuple():
    nested = (((1, 2), 'hey', '3'), ('q', 13, 'b'), ('3', 33, 333))
    print(nested)
    print(type(nested))

    for a, b, c in nested:
        print('*** TUPLE ***')
        print(a)
        print(b)
        print(c)



