
# Stop the Loop at 13

a = 1
for i in range(1,21):
    if(i==13):
        break
    print(i)
print()

#-------------------------------------------------------
# Guess correct number
 
secret = 7
for i in range(1,11):
    guess = int(input("Enter number:"))
    if(guess==secret):
        print("correct")
    else:
        print("Game over")
    
