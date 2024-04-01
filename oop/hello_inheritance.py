class Person:
    name = ""
    health = 100

    def __init__(self, name):
        print('Creating a person instance:', name)
        self.name = name

    def have_meal(self):
        print('Yummy ^^')
        self.health += 5

    def emotional_damage(self):
        print('0_o')
        self.health -= 1

    def print_info(self):
        print('My name is', self.name, '- Health level', self.health)


class Employee(Person):
    payroll = 0

    def print_info(self):
        super().print_info()
        print('Current payroll', self.payroll)

    def create_report(self):
        print('Report created by', self.name)
        self.payroll += 100
        self.emotional_damage()


e = Employee('Alice')
e.create_report()
e.have_meal()
e.create_report()
e.print_info()
