#Create a class Employee with attributes name and company_name = "TechCorp".
#Add a class method change_company(cls, new_name) to update the company name for all employees.
#Demonstrate how this change affects all instances.
class employee:
    def __init__(self,name,company_name):
        self.name = name
        self.company_name = company_name
    def change_company_name(self,cls,new_name):
        cls.company_name = self,new_name
