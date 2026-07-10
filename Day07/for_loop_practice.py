#program sum of even number

total = 0
for i in range(2,101,2):
  total+=i
  print("sum=" ,total)
------------------------------------------------
#program of factorial number
----------------------------------------------

num = int(input("Enter number:"))
fact = 1
for i in range(1,num,+1):
  fact = fact*i
  print("Factoral=",fact)
