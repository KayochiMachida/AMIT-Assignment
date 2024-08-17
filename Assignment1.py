"""
OOP SESSION
"""

class student :
    #attributes
    student_name= "kiko"
    student_age= 19
    student_GPA= 3.99
    student_gender= 'Male'

    #methods
    def student_info(self):
        print(f"student name = {self.student_name}")
        print(f"staudent age = {self.student_age}")
        print(f"student GPA = {self.student_GPA}")
        print(f"student gender = {self.student_gender}")

s1 =student()
s1.student_info()
print(s1.student_name)

from abc import ABC, abstractmethod


# Define an interface using an abstract base class
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


# Concrete class implementing the interface
class Dog(Animal):
    def move(self):
        print("Dog is running")

    def make_sound(self):
        print("Woof!")


# Another concrete class implementing the interface
class Fish(Animal):
    def move(self):
        print("Fish is swimming")

    def make_sound(self):
        print("Blub blub")


# Instantiate the concrete classes
dog = Dog()
dog.move()  # Output: Dog is running
dog.make_sound()  # Output: Woof!

fish = Fish()
fish.move()  # Output: Fish is swimming
fish.make_sound()  # Output: Blub blub


