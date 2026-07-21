a = int(input("Enter number :"))
b = int(input("Enter number :"))                      # prgm using fun to find greatest number
c = int(input("Enter number :"))

def greatest_num(a,b,c):
    if (a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif(c>a and c>b):
        return c
    else:
        print("Invalid number")

print(greatest_num(a,b,c))
    
#---------------------------------------------------------------------------    
# using fun to convert celsius to fahrenheit

c = float(input("Enter number :"))

def fahrenheit(c):
    f = (c*9/5)+32
    return f
print("Temperature in Fahrenheit =", fahrenheit(c))

#-------------------------------------------------------------------------------
# pattern
def pattern(n):
    if(n==0):
        return                
    print("*" * n)
    pattern(n-1)
pattern(10)
#------------------------------------------------------------------------------
# py prgm which convert inches to cms

def inch_cm(inches):
    return inches * 2.54            #2.54 is formula
n = int(input("Enter values in inches : "))
print(f"The corresponding value in cm {inch_cm(n)}")
    
#-------------------------------------------------------------------------------    
    
def remove_word(lst,word):               #lst used for receive list , word used for remove word
    new_list=[]                         #empty list
    for items in lst:
        if items.strip()!=word:
            new_list.append(items.strip())
            return new_list
        word = ["apple","banana","mango"," banana "," orange"]
        print(remove_word(word,"banana"))
  
#--------------------------------------------------------------------------------

#multipy

def multipy(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
multipy(7)
