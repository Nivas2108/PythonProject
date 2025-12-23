# . Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.
class Temperature:
    def __init__(self, celsius):
        self.celsius =celsius
    def show_conversion(self):
        fahrenheit=Temperature.to_fahrenheit(self.celsius)
        print(f"Fahrenheit={fahrenheit}")
    @staticmethod
    def to_fahrenheit(celsius):
        return celsius * 9/5 + 32

t1= Temperature(5)
t1.show_conversion()