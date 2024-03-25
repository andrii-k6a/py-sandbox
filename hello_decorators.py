import time
import math


def greetings_decorator(greetings_func):
    print('Before greetings')
    greetings_func()
    print('After greetings')


# @greetings_decorator calls a function, not just declares
@greetings_decorator
def greetings():
    print('Hello')


def execution_time_decorator(func):
    print('Adding execution time decorator...')

    def wrapper_func(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return wrapper_func


# @execution_time_decorator actually calls the execution_time_decorator function
# Equivalent would look like adding 'factorial = execution_time_decorator(factorial)' after factorial func declaration
@execution_time_decorator
def factorial(num):
    time.sleep(1)
    print('Result:', math.factorial(num))


factorial(10)
