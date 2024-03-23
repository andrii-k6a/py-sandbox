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


def key_value_iteration():
    data = {'banana': 10, 'apple': 3, 'strawberry': 23, 'dmt': 777}
    for k, v in data.items():
        print('Key:', k, 'Value:', v)


def enumerate_list():
    nums = [10, -15, 20, -25, 30, -35, 40, -45, 50]
    print(nums)

    for index, value in enumerate(nums):
        print(index, value)


def group_with_zip():
    l1 = [1, 3, 5, 7]
    l2 = ['a', 'c', 'a', 'b']
    l3 = ['q1', 'q2', 'x0', 'x1']

    for a, b, c in zip(l1, l2, l3):
        print('abc:', a, b, c)


def print_first_even(nums: list) -> None:
    for num in nums:
        if num % 2 == 0:
            print('Found even number', num)
            break
    else:
        # the block is being executed only if break was not hit in the loop body
        print('No even number')


# print_first_even([1, 3, 7, 9])
# print_first_even([1, 3, 42, 9])
