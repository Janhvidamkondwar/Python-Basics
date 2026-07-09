# --------------------------------------------
# Program 1: Print numbers from 0 to 10


for i in range(0, 11):
    print(i)



# --------------------------------------------
# Program 2: Print numbers from 10 to 1


for i in range(10, 0, -1):
    print(i)


# --------------------------------------------
# Program 3: Print numbers from 1 to 10


for i in range(1, 11):
    print(i)



# --------------------------------------------
# Program 4: Print even numbers from 2 to 20


for i in range(2, 21, 2):               #start = 2 , stop = 21, step =2
    print(i)



# --------------------------------------------
# Program 5: Print odd numbers from 1 to 19


for i in range(1, 20, 2):
    print(i)



# --------------------------------------------
# Program 6: Print numbers from 5 to 50


for i in range(5, 51, 5):
    print(i)

print()

# --------------------------------------------
# Program 7: Multiplication Table using for loop


n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print()

# -------------------------------------------------------
# Program 8: Greeting Names Starting with 's' by using list


names = ["sohan", "rohan", "sonal", "mohan", "suman", "sagar"]

for name in names:
    if(name.startswith("s")):
        print(f"Hello {name}")



#----------------------------------------------------------
# Program 9: Multiplication Table using while loop

a = int(input("Enter a number: "))
i = 1

while(i<=11):
    print(f"{a} x {i} = {a * i}")
    i += 1
