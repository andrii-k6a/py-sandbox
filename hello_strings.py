def concatenation():
    hello = 'hello'
    world = 'world'
    msg = hello + '_' + world + '!'
    print(msg)


def string_and_number_concatenation():
    message = 'the number is '
    number = 42
    print(message + str(number))


def number_as_string_concatenation():
    a = 7
    b = '123'
    print(a + int(b))


def print_letter():
    text = 'Hello There!'
    letter = text[6]
    print(letter)


def print_text_len():
    text = "This is text"
    print(text)
    print('The length of the text is', len(text))


def iterate_over_string():
    text = 'hello world'
    index = 0
    while index < len(text):
        symbol = text[index]
        print(index, symbol)
        index = index + 1


def iterate_over_string_2():
    text = 'hello world'
    index = 0
    for symbol in text:
        print(index, symbol)
        index = index + 1


def letter_frequency(letter: str, text: str) -> int:
    count = 0
    for symbol in text:
        if symbol == letter:
            count = count + 1
    return count
# print('The result is', letter_frequency('o', 'hello world'))


def char_numeric_representation():
    # ASCII - American Standard Code for Information Interchange - represents chars by numbers between 0 and 127(8 bits)
    # Unicode - a complex character set for all chars - not efficient to use for sending data across network, too large
    # UTF-8 / UTF-16 / etc. - subsets of Unicode to optimize memory efficiency (UTF-32 - almost full Unicode)
    # UTF-8 is best practice for data exchange across internet and its upwards compatible with ASCII

    # Since Python 3, all strings are represented by str type (same as unicode).
    # In Python 2 there were str and separate unicode type ( x = u'文' ) to represent chars
    # Also, in Python 2 and 3 strings might be represented by byte array ( x = b"abc" ) with some differences

    # Each char in a string is represented by number
    print('H -', ord('H'))
    print('E -', ord('E'))
    print('L -', ord('L'))
    print('L -', ord('L'))
    print('O -', ord('O'))


def slicing():
    text = 'Hello World'
    # first arg - start index, second arg - last index, but not including
    print(text[0:2])
    print(text[:2])
    print(text[6:9])
    print(text[6:])
    print(text[:])

    print('*** No tracebacks examples ***')
    # empty result
    print(text[10:5])

    # print to the end of the string
    print(text[1:333])


def in_as_logical_operator():
    fruit = 'apple'
    # it's like 'contains', also could be used with lists
    if 'app' in fruit:
        print('It contains app')
    if 'ple' in fruit:
        print('It contains ple')
    print('q' in fruit)
    print('Done')


def is_banana(word: str):
    if 'banana' == word:
        print('Yes, it is a banana!')
    else:
        print('No, it is not a banana')

    # lexicographic compression
    if 'banana' > word:
        print('Bigger than banana')
    else:
        print('Lower than banana')
# is_banana('banana')
# is_banana('HELLO')
# is_banana('hello')


def string_methods():
    greet = 'Hello Bob!'
    greet_lower = greet.lower()
    print(greet_lower)
    print(greet.find('Bob'))
    print(greet.find('Steven'))

    # it does not change the original object
    greet_replace = greet.replace('Bob', 'Jane')
    print(greet)
    print(greet_replace)
    # it replaces all, not only the first one
    print(greet.replace('o', 'X'))

    print('    Left strip'.lstrip())
    print('Right strip!    '.rstrip())
    print('    Strip!    '.strip())

    # Show attributes of an object
    print(dir(greet))

