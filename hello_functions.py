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


print('Start')
print_greetings()
print("The number is", add_magic_number(7))
print("The number is", add_magic_number())
# Cannot call functions that defined below
# print_max_and_min_of_word('Hello')
print('Done')


def print_max_and_min_of_word(word):
    for symbol in word:
        print(symbol)
    print('Max -', max(word))
    print('Min -', min(word))


print_max_and_min_of_word('FUN')


def assign_void_func():
    void = print('What if assign void func to a var?...')
    print('It would be', void)


assign_void_func()
