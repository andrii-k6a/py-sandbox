class Greetings:
    greeting = ''
    greetings_counter = 0

    def __init__(self, greeting):
        self.greeting = greeting
        print('Greetings constructor', self.greeting, self.greetings_counter)

    def hello(self):
        self.greetings_counter += 1
        print(self.greetings_counter, self.greeting)

    def __del__(self):
        print('Greetings destructor', self.greeting, self.greetings_counter)


g1 = Greetings('hello')  # Constructing an instance
g1.hello()  # Equivalent: Greetings.hello(g1)
g1.hello()
g1.hello()
Greetings.hello(g1)
print(type(g1))
print(dir(g1))

g1 = 'Destructor supposed to be called at this point'

g2 = Greetings('hola')
g2.hello()
g2.hello()

