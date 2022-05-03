# main file
# interface to access the account 
# menu options

from Customer import Customer
from Inventory import Inventory
import Cart as cart


print("--------  WELCOME TO THE BOOKSHOP  ------- \n")
print("---------------- GROUP_25 ----------------\n")
while True:
    print("1. LogIn \n2. Create Account \n3. Exit Program\n ")
    selectMenu = input("Select an option. ")
    
    ### select 1 to login
    if selectMenu == '1':
        userName = input("UserName : ")
        password = input("Password : ")
        customer = Customer(userName)
        # verifying the user account
        if customer.isUser()== True and customer.checkPassword(userName,password) == True:
            fName = customer.customersInfo.loc[customer.customersInfo['username'] == customer.userName, 'fname'].iloc[0]
            lName = customer.customersInfo.loc[customer.customersInfo['username'] == customer.userName, 'lname'].iloc[0]
            print(f"\n----- Welcome! {fName.upper()} {lName.upper()} --------")
            break
        elif customer.isUser()== False or customer.checkPassword(userName,password) == False:
            print("\nWrong UserName or Password, Try Again!\n")
        else:
            print("\nCouldn't verify account. Create an account.\n")

    ### select 2 to create account (new user)
    elif selectMenu == '2':
        print("\nCreating an Account\n")
        userName = input("UserName : ")
        password = input("Password : ")
        conf_password = input("Confirm Password : ")
        customer = Customer(userName)

        for i in range(2):    ## confirm password offers for 3 times
            if password != conf_password:
                print("Password did not match. Try Again!")
                conf_password = input("Confirm Password:")
          
        if password != conf_password: ## if not confirmed yet, start over
            print("Couldn't Match Password. Try Again!\n")
            continue
        
        else:  ## adds user to the customer csv file
            customer.addUser(userName,password)
            #verify = True ########
            print("\n------------- Creating Account -------------\n")
            firstname = input("Enter your First Name: ")
            lastname = input("Enter your Last Name: ")
            customer.setName(firstname,lastname)
            
            print("\nAccount Successfully Created.")
            print("\nWELCOME ", firstname.upper(), lastname.upper())
            print("\nEnter Shipping Address:")
            shipAddr = input("Enter Street Number and Name : ")
            shipCity = input("Enter the City : ")
            shipState = input("Enter the State : ")
            shipZip = input ("Enter the Zip: ")
            customer.setShippingAddress(shipAddr,shipCity,shipState,shipZip)
            break

    ### select 3 to exit the program.        
    elif selectMenu == '3':
        exit()
    
    ### any other input to loop back to menu options.
    else:
        print("Please select valid option.")

### For new menu options
if True:
    #### create inventory object ####
    inventory = Inventory()

    while True:
        print("\nSelect Options Below")
        options = input("\n(A) Account Info \n(I) Inventory Info \n(C) Cart Info \n(L) Log Out\n")

        ### second menu options
        if options.lower() == 'a':
            print("\n************* Account Information **************")
            editAccount = True
            ### Account infos
            while editAccount:
                print("\nACCOUNT OPTIONS:")
                accMenu = input("(A) View Account Information \n(U) Update Account Information\n(P) Edit Payment Information\n(O) View Order History\n(D) Delete Account\n(B) Return Back\n")
                
                viewAccount = True
                while viewAccount:
                    ### Account Details
                    if accMenu.lower() == 'a':
                        customer.printAccountDetails()
                        viewAccount = False
                    ### Update Acocunt Informations
                    elif accMenu.lower() == 'u':
                        ### Sub Menu for update account
                        accSubMenu = input ("(N) Update Name \n(S) Edit Shipping Address\n(B) Account Menu\n")
                        ### update name
                        if accSubMenu.lower() == 'n':
                            firstname = input("Update First Name: ")
                            lastname = input("Update Last Name: ")
                            customer.setName(firstname, lastname)
                            print("Account Updated Sucessfully.\n")  
                            viewAccount = False
                        ### update shipping address    
                        elif accSubMenu.lower() == 's':
                            shipAddr = input("Enter Street Number and Name : ")
                            shipCity = input("Enter the City : ")
                            shipState = input("Enter the State : ")
                            shipZip = input ("Enter the Zip: ")
                            customer.setShippingAddress(shipAddr,shipCity,shipState,shipZip)
                            viewAccount = False
                        ### Return back to account menu  
                        elif accSubMenu.lower() == 'b':
                            viewAccount = False

                    ### update payment informations    
                    elif accMenu.lower() == 'p':
                        print("\nUpdating Payment Information")
                        while True:
                            cardNum = input("Enter Card Number: ")
                            if cardNum.isnumeric() == True:
                                break
                            else:
                                print("Invalid entry. Please enter Numeric value only.")
    
                        cardName = input("Name on Card: ")
                        billAddr = input("Enter your Billing Address Street Number and Name: ")
                        billCity = input("Enter the city: ")
                        billState = input("Enter the State: ")
                        billZip = input("Enter the ZipCode: ")
                        customer.setPaymentInfo(cardName, cardNum, billAddr, billCity, billState, billZip)
                        viewAccount = False

                    elif accMenu.lower() == 'o':
                        cart.printOrderHistory()
                        viewAccount = False

                    elif accMenu.lower() == 'd':
                        customer.deleteAccount(cart)
                        # viewAccount = False

                    elif accMenu.lower() == 'b':
                        viewAccount = False

                    else:
                        print("Enter valid entry\n")
                        viewAccount = False
                
                if accMenu.lower() == 'b':
                    editAccount = False
        
        # prints inventory 
        elif options.lower() == 'i':
            inventory.printInventory()
        
        ## cart information selection
        elif options.lower() == 'c':
            cart = customer.getCart()
            editCart = True
            while editCart:
                cart.printCart()
                cartOption = input("\n1. Add to Cart\n2. View Cart\n3. View Inventory\n4. Delete Cart Item\n5. Checkout\n6. Return Back\n")
                if cartOption.lower() == '1':
                    ISBN = input("\nEnter ISBN number :")
                    quantity = int(input("\nItem Quantity :"))

                    if inventory.checkItemQuantity(ISBN, quantity):
                        cart.addToCart(ISBN, quantity)
                        inventory.delInventory(ISBN, quantity) ## reduce the quantity from inventory
                    else:
                        continue

                if cartOption.lower() == '4':
                    ISBN = input("\nEnter ISBN number to remove: ")
                    quantity = cart.checkCart(ISBN) ### might check if already empty, cart.print
                    inventory.addBackQuantity(ISBN,quantity) ### addQuantity
                    cart.removeFromCart(ISBN)

                elif cartOption.lower() == '2':
                    cart.printCart()

                elif cartOption.lower() == '3':
                    inventory.printInventory()

               
                elif cartOption.lower() == '5':
                    cart.checkout(inventory,customer)
                    editCart = False

                elif cartOption.lower() == '6':
                    editCart = False
                
                

        elif options.lower() == 'l':
            cart = customer.getCart()
            checkItems = cart.checkItems()
            if not checkItems:
                cart.addBackToInventory(inventory)
            customer.logout()




     
        