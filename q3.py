# Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.
class MathOps:
    @staticmethod
    def is_even(num):
        return num%2==0


obj=MathOps()
r=obj.is_even(4)
print(r)
#MathOps.is_even(3)
print(MathOps.is_even(5))

