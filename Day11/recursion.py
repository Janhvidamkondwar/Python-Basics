#recursion is function that calls itself

def num(n):
    if(n>5):
        return
    
    print(n)
    num(n+1)   #recursion is
num(1)


# factorial using recursion

def fac_rec(n):    #n is a parameter
    if n == 1:
        return(1)
        return n* fac_rec(n-1)
num = int(input("Enter number:"))
print("Factorial =" , fac_rec(num))

#countdown

def countdown(n):
    if (n==0):
        return
    
    print(n)
    
    countdown(n-1)
countdown(5)
