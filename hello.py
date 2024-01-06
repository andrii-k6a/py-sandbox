name = input('Enter your name: ')

while len(name) == 0:
    name = input('Please enter your name: ')

if name == 'anonymous':
    print('Hi, stranger!')
elif name == 'admin':
    print('Welcome back, sir!')
else:
    print('Welcome', name + '!', 'Have a nice one!')
