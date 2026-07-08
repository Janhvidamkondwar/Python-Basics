a1 = int(input("Enter math marks :"))
a2 = int(input("Enter Science marks : "))
a3 = int(input("Enter English marks :"))

#  total_percentage is  variable used for calcuculation

total_percentage = (a1 + a2 + a3) / 300 * 100

if(total_percentage >= 40 and a1>=33 and a2>=33 and a3>=33):
    print("You are passed",total_percentage)

else:
    print("You are failed" ,total_percentage)  
