def print_greetings():
    print('Hello from function!')
    print('See you around!')


def add_magic_number(value: int = 0) -> int:
    return value + 42


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def print_max_and_min_of_word(word):
    for symbol in word:
        print(symbol)
    print('Max -', max(word))
    print('Min -', min(word))


# print_max_and_min_of_word('FUN')


def assign_void_func():
    void = print('What if assign void func to a var?...')
    print('It would be', void)  # None


def nested_func_example():
    def add42(x: int):
        return x + 42

    magic_number_adder = add42  # function could be assigned to a variable
    print(type(magic_number_adder))  # <class 'function'>
    print(magic_number_adder(58))

    return magic_number_adder


def func_as_arg(func):
    magic_number = func(58)
    print(magic_number)


# func_as_arg(add_magic_number)
