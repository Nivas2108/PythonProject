# Q1. Create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
class Student:
    total_students = 0
    passing_mark = 40
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1
    def result(self):
        return "Pass" if self.marks >= Student.passing_mark else "Fail"
    @classmethod
    def apply_curve(cls, students, percentage, index=0):
        if index == len(students):
            return
        s = students[index]
        s.marks = min(100, s.marks + s.marks * percentage / 100)
        cls.apply_curve(students, percentage, index + 1)
    @staticmethod
    def letter_grade(marks):
        if marks >= 90:
            return 'A'
        elif marks >= 75:
            return 'B'
        elif marks >= 60:
            return 'C'
        elif marks >= 40:
            return 'D'
        else:
            return 'F'
    def display(self):
        print(
            self.name,
            "| Marks:", round(self.marks, 2),
            "| Result:", self.result(),
            "| Grade:", Student.letter_grade(self.marks)
        )
s1 = Student("Nivas", 82)
s2 = Student("Anu", 68)
s3 = Student("Rahul", 35)
students = [s1, s2, s3]
Student.apply_curve(students, 10)
for s in students:
    s.display()
print(s1.name,s1.marks)

# Q2. Design a class Product that:
# •	Maintains a base tax rate applicable to all products.
# •	Each product has a name and base price.
# •	Has a method to compute final price including tax.
# •	Can change tax rate for all products using one method.
# •	Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.	Creating multiple products.
# 2.	Changing the tax rate.
# 3.	Showing updated prices and validity checks.
class Product:
    # Class variable (shared by all products)
    tax_rate = 0.10   # 10% tax
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
    # Instance method: calculate final price
    def final_price(self):
        return self.base_price + (self.base_price * Product.tax_rate)
    # Class method: change tax rate for all products
    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate
    # Static method: validate price
    @staticmethod
    def is_valid_price(price):
        return price >= 0 and price <= 1_000_000  # realistic limit
p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 20000)
print("Initial Prices:")
print(p1.name, "Final Price:", p1.final_price())
print(p2.name, "Final Price:", p2.final_price())
Product.change_tax_rate(0.18)  # 18% tax
print("\nAfter Tax Rate Change:")
print(p1.name, "Final Price:", p1.final_price())
print(p2.name, "Final Price:", p2.final_price())
# Q3. Create an Employee class that:
# •	Keeps a minimum experience required for promotion (shared across all employees).
# •	Stores employee name, experience, and department.
# •	Has a method to check eligibility for promotion.
# •	Provides a function to update promotion criteria globally.
# •	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.	Creating employees from different departments.
# 2.	Changing promotion criteria.
# 3.	Displaying eligibility results and department validation.
class Employee:
    # Class variable (shared by all employees)
    min_experience_for_promotion = 3  # in years
    def __init__(self, name, experience, department):
        self.name = name
        self.experience = experience
        self.department = department
    # Instance method: check promotion eligibility
    def is_eligible_for_promotion(self):
        return self.experience >= Employee.min_experience_for_promotion
    # Class method: update promotion criteria
    @classmethod
    def update_promotion_criteria(cls, new_experience):
        cls.min_experience_for_promotion = new_experience
    # Static method: validate department
    @staticmethod
    def is_valid_department(department):
        valid_departments = ["HR", "Tech", "Admin"]
        return department in valid_departments
e1 = Employee("Alice", 2, "HR")
e2 = Employee("Bob", 5, "Tech")
e3 = Employee("Charlie", 4, "Admin")
print("Before changing promotion criteria:")
print(e1.name, "Eligible:", e1.is_eligible_for_promotion())
print(e2.name, "Eligible:", e2.is_eligible_for_promotion())
print(e3.name, "Eligible:", e3.is_eligible_for_promotion())
Employee.update_promotion_criteria(4)
print("\nAfter changing promotion criteria:")
print(e1.name, "Eligible:", e1.is_eligible_for_promotion())
print(e2.name, "Eligible:", e2.is_eligible_for_promotion())
print(e3.name, "Eligible:", e3.is_eligible_for_promotion())
# Q4. Build a Loan class that:
# •	Has a common interest rate for all loans.
# •	Each object stores borrower name and principal.
# •	Calculates total payable amount.
# •	Provides a function to update the interest rate.
# •	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.	Creating multiple loan accounts.
# 2.	Updating interest rates.
# 3.	Checking eligibility and total repayment for borrowers.
class Loan:
    # Class variable (shared interest rate)
    interest_rate = 0.10   # 10% interest
    def __init__(self, borrower_name, principal):
        self.borrower_name = borrower_name
        self.principal = principal
    # Instance method: calculate total payable amount
    def total_payable(self):
        return self.principal + (self.principal * Loan.interest_rate)
    # Class method: update interest rate
    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
    # Static method: check loan eligibility
    @staticmethod
    def is_eligible(salary):
        minimum_salary = 30000
        return salary > minimum_salary
l1 = Loan("Ravi", 200000)
l2 = Loan("Anita", 500000)
print("Before interest rate update:")
print(l1.borrower_name, "Total Payable:", l1.total_payable())
print(l2.borrower_name, "Total Payable:", l2.total_payable())
Loan.update_interest_rate(0.12)  # 12% interest
print("\nAfter interest rate update:")
print(l1.borrower_name, "Total Payable:", l1.total_payable())
print(l2.borrower_name, "Total Payable:", l2.total_payable())
#
# Q5. Create a class Course that:
# •	Tracks total courses created.
# •	Each course has a title, duration, and enrolled_students.
# •	Provides a method to enroll a new student.
# •	Allows updating the minimum duration for a valid course across all instances.
# •	Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.	Creating multiple courses.
# 2.	Enrolling students.
# 3.	Updating minimum duration and checking durations.
class Course:
    # Class variables
    total_courses = 0
    min_duration = 4   # minimum duration in weeks
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.enrolled_students = 0
        Course.total_courses += 1
    # Instance method: enroll a student
    def enroll_student(self):
        self.enrolled_students += 1
    # Class method: update minimum duration
    @classmethod
    def update_min_duration(cls, new_duration):
        cls.min_duration = new_duration
    # Static method: check if duration is realistic
    @staticmethod
    def is_valid_duration(duration):
        return duration > 0 and duration <= 104  # up to 2 years
c1 = Course("Python Programming", 12)
c2 = Course("Data Science", 24)
c1.enroll_student()
c1.enroll_student()
c2.enroll_student()
print("Course Details:")
print(c1.title, "Duration:", c1.duration,
      "Students:", c1.enrolled_students)
print(c2.title, "Duration:", c2.duration,
      "Students:", c2.enrolled_students)
print("Total Courses Created:", Course.total_courses)
Course.update_min_duration(6)
print("\nUpdated Minimum Duration:", Course.min_duration)

# Q6. Design a class Vehicle that:
# •	Keeps a record of service charge rate common to all vehicles.
# •	Each vehicle has a model, kilometers_run, and service history.
# •	Has a function to calculate service charge based on km and rate.
# •	Provides a method to update the service rate for all vehicles.
# •	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# 1.	Creating vehicles with different km and models.
# 2.	Updating the service rate.
# 3.	Showing charges and eligibility checks.
from datetime import datetime
class Vehicle:
    # Class variable (common to all vehicles)
    service_rate = 5   # charge per km
    total_vehicles = 0
    def __init__(self, model, kilometers_run, year):
        self.model = model
        self.kilometers_run = kilometers_run
        self.year = year
        self.service_history = []
        Vehicle.total_vehicles += 1
    # Instance method
    def calculate_service_charge(self):
        charge = self.kilometers_run * Vehicle.service_rate
        self.service_history.append(charge)
        return charge
    # Class method to update service rate for all vehicles
    @classmethod
    def update_service_rate(cls, new_rate):
        cls.service_rate = new_rate
    # Static method to check eligibility
    @staticmethod
    def is_eligible_for_service(year):
        current_year = datetime.now().year
        return (current_year - year) <= 15
v1 = Vehicle("Honda City", 12000, 2015)
v2 = Vehicle("Maruti Alto", 8000, 2012)
v3 = Vehicle("Hyundai i20", 15000, 2005)
print("Service Charge v1:", v1.calculate_service_charge())
print("Service Charge v2:", v2.calculate_service_charge())
##############################################
class mode:
    character="good"
    height=5
    entire_mode=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        mode.entire_mode+=1
    def after_change(self):
        diff=self.age+2
        return diff
    @classmethod
    def change_character(cls,new_character,new_height):
        cls.character=new_character
        cls.height=new_height
c1=mode("nivas",56)
print("after change in age the age is:",c1.after_change())
###################################################
# Q7. Build an Inventory class that:
# •	Tracks the total number of items across all inventories.
# •	Each instance maintains its own stock dictionary ({"item": quantity}).
# •	Provides a method to add or remove stock.
# •	Allows updating a minimum stock threshold globally.
# •	Offers a static checker to verify if a stock level is below threshold.
# Demonstrate:
# 1.	Managing multiple inventories.
# 2.	Adjusting stock threshold.
# 3.	Using static validation inside the instance logic.
class Inventory:
    # class variables
    total_items = 0
    min_stock_threshold = 5
    def __init__(self, name):
        self.name = name
        self.stock = {}   # instance-specific stock
    def update_stock(self, item, quantity):
        # get old quantity
        old_qty = self.stock.get(item, 0)
        # update quantity
        new_qty = old_qty + quantity
        if new_qty < 0:
            print(f"Cannot remove more {item} than available in {self.name}")
            return
        self.stock[item] = new_qty
        # update global total items
        Inventory.total_items += quantity
        # static validation inside instance logic
        if Inventory.is_below_threshold(new_qty):
            print(f"⚠️ Warning: {item} stock is below threshold in {self.name}")
    @classmethod
    def update_min_threshold(cls, new_threshold):
        cls.min_stock_threshold = new_threshold
    @staticmethod
    def is_below_threshold(quantity):
        return quantity < Inventory.min_stock_threshold
    def display_stock(self):
        print(f"{self.name} Inventory:", self.stock)
# Q8. Create a HotelRoom class that:
# •	Keeps a base price per night (shared).
# •	Each room has room_number, nights_booked, and guest_name.
# •	Has a method to calculate total bill.
# •	Allows updating the base price across all rooms.
# •	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
# Demonstrate:
# 1.	Creating rooms and bookings.
# 2.	Changing base price.
# 3.	Checking bill updates and validation.
class HotelRoom:
    base_price=500
    def __init__(self,room_number,nights_booked,guest_name):
        self.room_number=room_number
        self.nights_booked=nights_booked
        self.guest_name=guest_name
    def total_bill(self):
        total=HotelRoom.base_price*self.nights_booked
        print(total)
    @classmethod
    def update_baseprice(cls,new_price):
        cls.base_price=new_price
    @staticmethod
    def validity(nights):
        if nights<=0:
            print("atleast one night ")
        else:
            print("valid")
a1=HotelRoom(2,3,"nivas")
a2=HotelRoom(1,0,"raj")
HotelRoom.total_bill(a1)
HotelRoom.total_bill(a2)
HotelRoom.validity(a2.nights_booked)
# Q9. Design a LibraryMember class that:
# •	Tracks total active members.
# •	Each member has a name and books_borrowed count.
# •	Has a function to borrow books, with borrowing limit common to all.
# •	Allows updating borrowing limit globally.
# •	Has a static function to check if book title is valid (non-empty string, reasonable length).
# Demonstrate:
# 1.	Borrowing books for multiple users.
# 2.	Changing borrowing limits.
# 3.	Validating book titles before borrowing.
class LibraryMember:
    borrowing_limit=2
    total_active_members=0
    def __init__(self,name,title,books_borrowed_count):
        self.name=name
        self.title=title
        self.books_borrowed_count=books_borrowed_count
    def borrow_books(self):
        if self.books_borrowed_count<LibraryMember.borrowing_limit:
            print("u have limit")
        else:
            print("out of limit")
    @classmethod
    def update(cls,new_limit):
        cls.borrowing_limit=new_limit
    @staticmethod
    def check_title(title):
        if len(title)==0:
            print("empty string")
        else:
            print("borrow book")
x1=LibraryMember("nivas","man",1)
x2=LibraryMember("madhu","silent",4)
x1.check_title(x1.title)
LibraryMember.borrow_books(x1)
LibraryMember.borrow_books(x2)
LibraryMember.check_title(x2.title)
# Q10. Create a class Member that:
# •	Has a shared BMI limit for “fit” status.
# •	Each member stores name, height, weight.
# •	Has a method to calculate BMI and check fit status.
# •	Provides a function to update BMI limit for all members.
# •	Offers a tool to check if height and weight entered are valid numbers.
# Demonstrate:
# 1.	Creating multiple members.
# 2.	Updating BMI standard.
# 3.	Displaying fit status and input validity
class Member:
    BMI_limit=60
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def calculate_BMI(self):
        self.bmi=self.weight//self.height**2
        if self.bmi<=Member.BMI_limit:
            print("u are fit")
        else:
            print("not fit")
    @classmethod
    def update(cls,new_limit):
        cls.BMI_limit=new_limit
    @staticmethod
    def check(height,weight):
        if height<0 and weight<0:
            print("not valid")
        else:
            print("valid")
m1=Member("nivas",164,55)
m2=Member("mad",170,62)
m1.check(m1.height,m1.weight)
m2.check(m2.height,m2.weight)
Member.calculate_BMI(m1)
Member.calculate_BMI(m2)
