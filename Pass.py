#Imports
import random
import string

#Define
def Ask():  
    #Ask
    while True:
        Again = input("New Password? (Y/N)")
        if Again == "y" or Again == "Y":
    
            #Setup Variables
            #Input Length
            while True:
                user_input = input("Password Length:")
                if user_input.isdigit():
                    Length = int(user_input)
                    print("Valid Input... Proccessing")
                    break
                else:
                    print("Invalid Input... Please Try Again")
                
            #Final Product
            password = ""

            #Generate Characters
            for i in range(Length):
                Char = str(random.choice(string.ascii_letters + string.digits + string.punctuation))
                password += Char

            #Output Password
            print(password)
            
        elif Again == "n" or Again == "N":
            print("Thank You. Have A Nice Day :)") 
            break

        else:
            print("Invalid Input... Please Try Again")

#First Call
Ask()
