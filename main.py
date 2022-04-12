from os import system ,name
#Function is used to create account
def create_ACC():
    print("Enter your Username \n")
    Username = input()
    print("Enter Password")
    Password = input()
    #writes Username and Password to CSV 

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
    #If they match return true
def Exit():
    return False

def Loop():
    return True
#Menu Options before user is logged in
def MenuOptionsBeforeLogin(input):
    clear()

    switcher ={
        0: login(),
        1: Exit(),
        2: print("test"),
    }
    switcher.get(input,"nothing")
    
    
def main():
  
    print("hello")


if __name__ == "__main__":
    while(True):
        
        MenuOptionsBeforeLogin()


