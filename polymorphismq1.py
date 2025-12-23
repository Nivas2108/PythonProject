# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().
class animal:
    def make_sound(self):
        print("animal in X")
class dog(animal):
    def make_sound(self):
        print("dog in X")
class cat(animal):
    def make_sound(self):
        print("cat in X")
class cow(animal):
    def make_sound(self):
        print("cow in X")
def calling_make_sound(x):
    x.make_sound()
obj=animal()
obj1=dog()
obj2=cat()
calling_make_sound(obj)
calling_make_sound(obj1)
calling_make_sound(obj2)
