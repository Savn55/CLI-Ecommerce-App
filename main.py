from os import system ,name

from Customer_Interface import *
#Function is used to create account
def create_ACC():
    print("Enter your Username \n")
    Username = input()
    print("Enter Password")
    Password = input()
    #writes Username and Password to CSV 

def PreMenu():
    print("Menu Options")
    print("1. ")

def clear():
    if name == 'nt':
        _ = system('cls ')

    else: 
        _ = system('clear')

#Function used for logging into account
def login():
    clear()
    print("Enter Username to login\n")   
    Username = input()
    print("Enter Password")
    Password = input()
    #Needs to check Username and Password from file
    User = Account("N/a","N/a","N/a","N/a","n/a",Username,Password)
    User.Set_Password(Password)
    User.Set_Username(Username)
    
    if User.check_accounts():
        print("Login Successful\n")
        User.State = True
        return True
    else:
        print("Login Failed\n")
        return False
    #If they match return true
def Exit():
    return False

def Loop():
    return True
#Menu Options before user is logged in

    
    
def main():
    Account.create_account()
    


if __name__ == "__main__":
    main()

           


