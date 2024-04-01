print('*** Decorators with args ***')


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
