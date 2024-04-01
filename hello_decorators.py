import time
import math


print('*** Greetings decorator ***')


def greetings_decorator(greetings_func):
    print('Before greetings')
    greetings_func()
    print('After greetings')


# @greetings_decorator calls a function, not just declares
@greetings_decorator
def greetings():
    print('Hello')


print('\n*** Timer decorator ***')


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


print('\n*** Decorators chain ***')


def multiply_by_10(func):
    print('Wrapping with multiply_by_10')

    def inner():
        print('Calling outer func from inner multiply_by_10')
        num = func()
        print('Multiplying by 10 for number', num)
        return num * 10
    return inner


def add_42(func):
    print('Wrapping with add_42')

    def inner():
        print('Calling outer func from inner add_42')
        num = func()
        print('Adding 42 for number', num)
        return num + 42

    return inner


@multiply_by_10
@add_42
def num1():
    print('Returning 10 from num1')
    return 10
# Equivalent: num1 = multiply_by_10( add_42( num1 ) )  Notice that num1 is a ref to a func, it doesn't call num1()


print('About to call num1()')
print('Num1 result', num1(), '\n')  # 520


@add_42
@multiply_by_10
def num2():
    print('Returning 10 from num2')
    return 10
# Equivalent: num1 = add_42( multiply_by_10( num2 ) )  Notice that num2 is a ref to a func, it doesn't call num2()


print('About to call num2()')
print('Num2 result', num2())  # 142


print('\n*** Decorators with args ***')


def foo(number, description):
    print('hello from foo -', number, description)

    def inner_decorator(f):
        print('hello from foo.inner_decorator')

        def wrapped(*args, **kwargs):
            print('hello from foo.inner_decorator.wrapped')
            result = f(*args, **kwargs)
            print('bye from foo.inner_decorator.wrapped')
            return result

        print('bye from foo.inner_decorator')
        return wrapped

    print('bye from foo')
    return inner_decorator


@foo(42, 'example')
def bar():
    print('hello from bar')
    return 'I am bar func'
# Equivalent: 'bar = foo(42, 'example')(bar)'


print('Calling bar!..')
print(bar())
