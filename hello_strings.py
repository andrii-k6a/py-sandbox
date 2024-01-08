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


def slicing():
    text = 'How to slice a string into slices?'
    # first arg - start index, second arg - last index, but not including
    print(text[0:3])
    print(text[4:6])
    print(text[7:12])
    print(text[15:21])

    print('*** No tracebacks examples ***')
    print(text[10:5])
    index_out_the_len = len(text) + 3
    print(text[15:index_out_the_len])


