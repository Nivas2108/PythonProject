class transport:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def move(self):
        print("vehicle are moving fast")
class bus(transport):
    def __init__(self, name, price,colour):
        super().__init__(name, price)
        self.colour = colour
    def move(self):
        print("bus moves slow")
obj = bus('schoolbus ',120000,'yellow')
obj.move()
print(obj.name)
print(obj.price)
obj1=transport('Bobby',120)
obj1.move()
print(obj1.name)