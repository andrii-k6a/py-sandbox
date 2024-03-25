class Greetings:
    greetings_counter = 0

    def hello(self):
        self.greetings_counter += 1
        print(self.greetings_counter, 'Hello')


g1 = Greetings()  # Constructing an instance
g1.hello()  # Equivalent: Greetings.hello(g1)
g1.hello()
g1.hello()
Greetings.hello(g1)
print(type(g1))

g2 = Greetings()
g2.hello()
g2.hello()

