def print_greetings():
    print('Hello from function!')
    print('See you around!')


def add_magic_number(value: int = 0) -> int:
    return value + 42


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
