def line_by_line_reading():
    reader = open('resources/poem.txt', 'r')
    line_counter = 0

    for line in reader:
        line_counter = line_counter + 1
        print(line, end='')

    print('\n***********')
    print("The number of lines in the poem is", line_counter)


def whole_file_reading():
    reader = open('resources/poem.txt', 'r')
    text = reader.read()
    print('The text len is', len(text), '\n')
    print(text[:132])


def find_line_in_file():
    reader = open('resources/poem.txt', 'r')
    for line in reader:
        # strip the new line at the end of the line
        line = line.rstrip()
        if line.startswith('Stars'):
            print(line)
    print('Done')


def check_if_line_contains_using_in_operator():
    reader = open('resources/poem.txt', 'r')
    for line in reader:
        if 'of' not in line:
            continue
        print(line.rstrip())
    print('Done')


def read_file_provided_from_input():
    filename = input('Enter a file name: ')
    filename = filename.strip()

    try:
        reader = open('resources/' + filename)
    except:
        print('Cannot open the file', filename)
        quit()

    counter = 0
    # notice that reader in accessible out of the try block
    for line in reader:
        if 'universe' in line:
            counter = counter + 1
    print('The amount of universe:', counter)


