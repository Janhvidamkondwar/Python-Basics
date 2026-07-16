#program of cube

def cube(n):
    if(n>5):
        return 

    print(n*n*n)
    cube(n+1)
cube(1)

# program of odd

def odd(n):
    if(n>9):
        return
    
    print(n)
    odd(n+2)
odd(1)

# print even number
def even(n):
    if(n>10):
        return

    print(n)
    even(n + 2)

even(2)
    

        
