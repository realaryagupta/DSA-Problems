# Object literal is an easy way to create objects 
'''
L = [1,2,3,4]
L.append
'''

# Bank ATM Project
class ATM:
    '''
    Methods are fxn that are written inside a class generally written like L.append like this with dot
    Normal Fxn are fxn that are written anywhere else  written like len(L) and like this 
    '''

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input(" 1. To create Pin \n 2. To ENTER Pin \n 3. Enter to withdraw \n 4. Check Balance \n 5. Exit")

        if user_input == "1":
            print("Create Pin")
            self.create_pin()

        elif user_input == "2":
            print("Withdraw")
            self.withdraw()
            
        elif user_input == "3":
            print("Deposit")
            self.deposit()

        elif user_input == "4":
            print("Balance")
            self.balance()

        else:
            print("Bye")
    
    def create_pin(self):
        self.pin = input("Enter Pin")
        print("Pin Set Sucess")

    def deposit(self):
        temp = int(input("Enter the Pin"))

        if temp == self.pin:
            amount = int(input("Enter your amount"))
            self.balance = self.balance + amount
        
        else:
            print("invalid pin")

    def withdraw(self):
        temp = int(input("Enter the Pin"))

        if temp == self.pin:
            amount = int(input("Enter amount to withdraw"))

            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation sucess")
            else:
                print("less funds")
        
        else:
            print("invalid pin")

    def balance(self):
        temp = int(input("Enter Pin"))

        if temp == self.pin:
            print(f"Account balance is {self.balance}")

sbi = ATM()
