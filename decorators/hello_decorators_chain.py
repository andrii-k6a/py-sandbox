print('*** Decorators chain ***')


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
