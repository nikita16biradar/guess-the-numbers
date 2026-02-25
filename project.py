import random
target= random.randint(1,100)
while True:
    userChoice =  input("Guess the traget or Quit :")
    if(userChoice == "Quit"):

        break
    userChoice = int(userChoice)
    if(userChoice == target):
       print("Success : Correct Guess!!")
       break
    elif(userChoice < target):
        print("your number was tooo small.Take a bigger guess...")
    else:
     
     print("your number was tooo big.Take a bigger guess...")


print("--------------GAME OVER----------")


  
    

