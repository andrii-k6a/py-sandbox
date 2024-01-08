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

