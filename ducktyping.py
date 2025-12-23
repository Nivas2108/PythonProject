class Dog:
    def quack(self):
        print("Dog")
class Duck:
    def quack(self):
        print("Duck")
def make_it_speak(x):
    x.quack()
dogesh=Dog()
quackesh=Duck()
make_it_speak(dogesh)
make_it_speak(quackesh)