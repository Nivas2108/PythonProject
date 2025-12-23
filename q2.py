#  Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.
class employee:
    company_name=" Techcorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change(cls,name):
        cls.company_name=name
obj=employee("Nivas")
obj1=employee("harsha")
print("before changing company")
print(f"{obj.name}{obj.company_name}")
print(f"{obj1.name}{obj1.company_name}")
print("after changing company")
employee.change(" cvcorp")
print(f"{obj.name}{obj.company_name}")
print(f"{obj1.name}{obj1.company_name}")


