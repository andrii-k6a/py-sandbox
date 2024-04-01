print('*** Greetings decorator ***')


def greetings_decorator(greetings_func):
    print('Before greetings')
    greetings_func()
    print('After greetings')


# @greetings_decorator calls a function, not just declares
@greetings_decorator
def greetings():
    print('Hello')
