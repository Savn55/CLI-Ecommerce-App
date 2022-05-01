from pickle import TRUE
from sqlite3 import adapt
import csv
from venv import create

from main import *
#Book Class
class Book:
    def __init__(self,Name,Author,ISBN,Quantity):
        self.Name = Name
        self.Author = Author
        self.ISBN = ISBN
        self.Quantity = Quantity
    
class Account:
    def __init__(self,First,Last,Address,Email,Username,Password,State):
        self.First = First
        self.Last = Last
        self.Address = Address
        self.Email = Email
        self.Username = Username
        self.Password = Password
        self.State = State
    def Get_Username(account):
        return account.Username
    def Get_Password(account):
        return account.Password
    def Set_Password(self,password,):
        self.Password = password
    def Set_Username(self,username):
        self.Username = username
    def Get_Account_state(self):
        return self.State
    def Get_Account_Row(Username):
        with open('Customer.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if(row[2] == Username):
                    return row

  #should return to login screen but exits for now
    def logout(self):
        self.State = False
        exit()

    def check_accounts(self):
        with open('Customer.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if(row[2] == self.Username and row[3] == self.Password):
                    return TRUE

    #Create Account Function, Returns True if account is created and False if account already exists
    def create_account():
        print("Enter your First Name")
        First = input()
        print("Enter your Last Name")
        Last = input()
        print("Enter your Address")
        Address = input()
        print("Enter your Email")
        Email = input()
        print("Enter your Username")
        Username = input()
        print("Enter your Password")
        Password = input()
        State = False
        User = Account(First,Last,Address,Email,Username,Password,State)
        with open('Customer.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if(row[2] == Username or row[3] == Password or row[4] == Email):
                    print("Account already exists")
                    return False
        with open('Customer.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([User.First,User.Last,User.Username,User.Password,User.Email,User.Address,User.State])
            return True

                    
                  

                    

    

        

        

    