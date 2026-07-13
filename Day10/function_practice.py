#positive or negative number

def check_number(num):
    if(num>0):
        print("Positive number")
    elif(num<0):
        print("Negative number")
    else:
        print("Zero")
n = int(input("Enter number : "))
check_number(n)


#Greatest of 3 Numbers

a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
def number(a ,b,c):
    if(a>b and a>c):
        print("The greatest number is :" , a)
    elif(b>a and b>c):
        print("The greatest number is :" , b)
    elif(c>a and c>b):
        print("The greatest number is :" , c)
    else:
        print("zero")
number(a,b,c)
        
        
