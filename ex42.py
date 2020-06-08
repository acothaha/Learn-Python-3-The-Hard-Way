# Is-A, Has-A, Objects, and Classes

# Animel is-a objetct (yes, sort of counfusing) look at the example

class Animal(object):
    pass

## dog is an Animal
class Dog(Animal):
    def __init__(self, name):
        ## A dog has a name attach to it
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## A cat has a name attach to it
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## A person has-a name attach to her/him
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ## An employee has-a salary within them

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## Rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("mary")

## mary has-a Cat pet named satan
mary.pet = satan

## frank is-a employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a dog pet named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
