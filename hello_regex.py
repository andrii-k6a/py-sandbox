# Python Regular Expression Quick Guide
#
# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

import re


def hello_regex():
    poem = open('resources/poem.txt')
    for line in poem:
        line = line.strip()
        if re.search('the', line):
            print(line)


def start_with_by_regex():
    poem = open('resources/poem.txt')
    for line in poem:
        line = line.strip()
        if re.search('^Nature.*', line):
            print(line)


def find_all_numbers():
    text = 'There are 2 types. For example, 42. Or could have been 101010.'
    numbers = re.findall('[0-9]+', text)
    print(numbers)
    print(type(numbers))
    print(type(numbers[0]))
    print(re.findall('[0-9]+', 'Nu numbers here'))


def find_chars():
    text = 'There are 2 types. For example, 42. Or could have been xxx.'
    result = re.findall('[ex]+', text)
    # result - ['e', 'e', 'e', 'e', 'ex', 'e', 'e', 'ee', 'xxx']
    print(result)


def greedy_matching():
    msg = 'Subject: Super Important: It is a good time to sell'
    # match the largest possible string - 'Subject: Super Important:', not just 'Subject:'
    # + and * are greedy
    res = re.findall('^S.+:', msg)
    print(res)


def non_greedy_matching():
    msg = 'Subject: Super Important: It is a good time to sell'
    # match the shortest possible string - 'Subject:', not whole 'Subject: Super Important:'
    # +? and *? - question mark makes it non-greedy
    res = re.findall('^S.+?:', msg)
    print(res)


def fine_tuning_string_extraction():
    header = 'From dr.drums@corp.com 01/01/2999 Hello from the Future'
    print(header)

    email = re.findall('\\S+@\\S+', header)
    print(email)

    # ( and ) - parentheses - they are not part of the match,
    # but they tell where to start and stop what string to extract
    email_with_parentheses = re.findall('^From (\\S+@\\S+)', header)
    print(email_with_parentheses)


def find_email_hosts():
    text = 'From: hello@python.org - Subject: Regex. CC: hello@world.com'
    print(text)

    all_hosts = re.findall('@([^ ]*)', text)
    print('All hosts:', all_hosts)

    sender_host = re.findall('^From: .+?@([^ ]*)', text)
    print('Sender host:', sender_host)

    cc_host = re.findall('Subject: .+?CC: .+?@([^ ]*)', text)
    print('CC host:', cc_host)


def max_price():
    data = [
        'The price - 42.10101$',
        'The price - 7$',
        'The price - 100.01$',
        'The price - 199.99$ now',
        'The price - 999',
        'This is number - 111$',
        'The price - -5$',
    ]

    numbers = list()
    for data_item in data:
        # notice the escaping of the dollar sign with double backward slashes at the end
        # it does not require the line to be ended
        value = re.findall('^The price - ([0-9.]+)\\$', data_item)
        if len(value) > 0:
            number = float(value[0])
            numbers.append(number)

    print(numbers)
    print('The highest price is ', max(numbers))


max_price()
