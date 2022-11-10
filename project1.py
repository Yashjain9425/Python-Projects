import random

print("THIS IS A DICE GAME IN EVERY CORRECT ANS YOU GETS THE 10 POINTS")
print("ALL THE BEST , ENJOY THE GAME")
print("If you want to exit the game enter 0")
s = 0
while(True):
    a=random.randint(1,6)
    
    x=int(input("write your number :"))
    print("dice comes to :",a)
    if x ==a:
        print("congratulations your number is correct and YOU GETS THE 10 POINTS")
        s = s + 10
        print("now your point is",s) 
    elif x == 0:
        print("Thank you for playing")
        print("our total score is",s)
        break
      
