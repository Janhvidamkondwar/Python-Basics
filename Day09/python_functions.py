
# 1. Star Pattern
# ------------------------------------------

for i in range(3, 9):
    print("*" * i)


# ------------------------------------------
# 2. Reverse Multiplication Table
# ------------------------------------------

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {11-i} = {n * (11-i)}")


# ------------------------------------------
# 3. Simple Function
# ------------------------------------------

def hello():
    print("Hello")

hello()


# ------------------------------------------
# 4. Good Day Function
# ------------------------------------------

def good_day():
    print("Good Day")

good_day()


# ------------------------------------------
# 5. Greeting Function (Parameter)
# ------------------------------------------

def greet(name):
    print("Hello", name)

greet("Janhvi")
greet("Rohan")


# ------------------------------------------
# 6. Greeting with User Input
# ------------------------------------------

name = input("Enter your name: ")

def greet_user():
    print("Hello", name)

greet_user()


# ------------------------------------------
# 7. Addition Function
# ------------------------------------------

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def add():
    print("Addition =", a + b)

add()


# ------------------------------------------
# 8. Square Function
# ------------------------------------------

n = int(input("Enter a number: "))

def square():
    print("Square =", n * n)

square()


# ------------------------------------------
# 9. Cube Function (Parameter)
# ------------------------------------------

def cube(num):
    print("Cube =", num * num * num)

n = int(input("Enter a number: "))
cube(n)


# ------------------------------------------
# 10. Even or Odd Function
# ------------------------------------------

def even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

n = int(input("Enter a number: "))
even_odd(n)


# ------------------------------------------
# 11. Largest Number Function
# ------------------------------------------

def largest_num(a, b):
    if a > b:
        print("The largest number is:", a)
    elif b > a:
        print("The largest number is:", b)
    else:
        print("Both numbers are equal")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest_num(a, b)
