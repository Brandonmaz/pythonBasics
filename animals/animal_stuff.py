# Parent animal class
class Animal:
    def __init__(self, name):
        self.animal_name = name

    def eat(self):
        raise NotImplementedError("Child class should be implementing this")


# Child class
class Monkey(Animal):
    def eat(self):
        print("monkey eating bananas...")


class Bird(Animal):
    def eat(self):
        print("bird eating seeds...")

    def fly(self):
        print("bird soaring high...")


my_monkey = Monkey("Joe")
my_monkey.eat()

my_bird = Bird("Jared")
my_bird.fly()
