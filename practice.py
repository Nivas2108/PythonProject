# 1.Write a program to convert kg to g. (Input 5.6kg print in grams)
n=5.6
g=int(n*1000)
print(f"{g} grams")
# 2.Write a program to covert temperature from degree C to F. (Input 80C)		(80°C × 9/5) + 32 = 176°F
t=80
f=int(t*9/5+32)
print(f"{f} fahrenheit")
# 3.Declare and initialize 3 three variable and print the biggest number.
a=1
b=3
c=8
if a>b & a>c:
    print(a)
if b>a &b>c:
    print(b)
else:
    print(c)
# 4.	Write a python program that performs the following tasks.
# a.	Store a number in a variable
# b.	If value is not in range (100-1000) prints wrong number else follows the steps
# c.	Check even or odd
# d.	If even divide the number by 3 and print the remainder
# e.	If odd divide the number by 2 and print the remainder.
n=10
if 100<=n>=1000:
    if n%2==0:
        print(n%3)
    else:
        print(n%2)
else:
    print("wrong number")
# 5.Declare & initialize a number. Check whether the number is in range 0-100 or not.
# If not in range print invalid input. Else – if the number is in range 91-100 then print
# Super Smart, 81-90 print Smart,71-80 print smart enough, 61-70 print just smart
# , 36-60 print no smart, 0-35 print dump.
n=56
if 0<=n<=100:
    if 91<=n<=100:
        print("super smart")
    elif 81<=n<=90:
        print("smart")
    elif 71<=n<=80:
        print("smart enough")
    elif 61<=n<=70:
        print("just smart")
    elif 36<=n<=60:
        print("no smart")
    elif 35<=n<=35:
        print("dump")
else:
    print("invalid input")
# 6.	Write a program to perform simple math based on the user inputs by using Switch condition.(+ , - , * , /)
a=7
b=10
match("-"):
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
# 7.Write a program to print CVCORP for 33 times.
n="CVCORP"
print(n*33)
# 8.Write a program to print all numbers which are divisible by 11 from 250 to 550.
for i in range(250,550):
    if i%11==0:
        print(i)
# 9.Write a program to sum all the numbers from 56 to 153.
s=0
for i in range(56,154):
   s=s+i
print(s)
# 10.Write a program to print all even numbers in range 700 to 900.
for i in range(700,900):
    if i%2==0:
        print(i)

