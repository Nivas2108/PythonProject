# Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.
class car:
    wheels=4
    mileage=20

    def display_specs(self):
        print(f"mileage={self.mileage},wheels:{car.wheels}")
    @classmethod
    def change_wheels(cls,new_wheel,new_mileage):
        cls.wheels=new_wheel
        cls.mileage=new_mileage
print(car.wheels,car.mileage)
car.change_wheels(5,5)
print(car.wheels,car.mileage)


