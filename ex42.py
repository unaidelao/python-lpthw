## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):
	
	def __init__(self, name):
		## Cat has-a name
		self.name = name
	
## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name. 'super' calls Person class constructor for 'name' attribute
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a Fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass
	

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## satan is Mary's pet
mary.pet = satan

## frank is-a Employee, so... is also a Person
frank = Employee("Frank", 120000)

## rover is Frank's pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon, so... is also a Fish
crouse = Salmon()

## harry is-a Halibut, so... is also a Fish
harry = Halibut()