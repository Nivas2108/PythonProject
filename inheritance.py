# Create a base class Transport with move() and derived classes Bus
#  and Bike, which have the same "move" method but with different behaviour
#  it but also call the parent implementation using super().
class Transport:
    def move(self):
        print("Moving")
class Bike(Transport):
    def move(self):
        print("Bike")
        super().move()
class Bus(Transport):
    def move(self):
        print("Bus")
        super().move()
bike1=Bike()
bus1=Bus()
bike1.move()
bus1.move()