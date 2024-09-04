# Default value is created when the function is defined, not when the function is called
# Therefore mutable object as default value is a bad practice
def surprise(my_list=[]):
    print(my_list)
    my_list.append('surprise!')


surprise()
surprise()
surprise()


# It prints the following instead of an empty list all the time:
# []
# ['surprise!']
# ['surprise!', 'surprise!']

# The right way to implement it:
def no_surprise(my_list=None):
    if my_list is None:
        my_list = []
    print(my_list)
    my_list.append('no surprise!')


no_surprise()
no_surprise()
