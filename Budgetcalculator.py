class Budget:

    def __init__(self,category,balance = 0):
        self.category = category
        self.balance = balance
    
    def withdraw(self,withdrawamount):
        
        if self.balance > withdrawamount:
            self.balance = self.balance - withdrawamount
            return True
        else:
            print("Not enough money")
            return False
  

    def deposit(self,depositamount):
        
        self.balance = self.balance + depositamount




def add_categories(categories):
    addcat = len(categories) + 1
    while len(categories) < addcat:
        cat = input("Enter a category name: ").capitalize()
        addvalue = (Budget(cat),)
        categories = categories + addvalue
        return categories

    
def get_balance():
    balance = int(input("Enter your budget balance: "))
    return balance


def get_choice(categories):
    check = False
    
    while check == False:
        userchoice1 = input("Enter category or type L to list them: ").lower()
    
        for i in categories:
        
            if userchoice1 == "l":
                print(i.category)
                
            elif userchoice1 == i.category.lower():
                check = True
                break
        
    return i       
    

def get_deposit_or_withdraw():
    userchoice = input("Enter d or w: ")
    if userchoice == "d":
        return 0
    if userchoice == "w":
        return 1

def withdraw_deposit(choice,depo_or_with,balance):
    
    if depo_or_with == 0:
        h = int(input("Amount to deposit: "))
        if balance >= h:
            choice.deposit(h)
            balance = balance - h
        else:
            print("Not enough")
        
    if depo_or_with == 1:
        s = int(input("Amount to withdraw: "))
        if choice.withdraw(s) == True:
            balance = balance + s
    return balance

def check_balance(categories):
    for i in categories:

        print(i.category,"has a balance of", i.balance)
    



def Main():
    balance = 0
    categories = Budget("Food"),Budget("Entertainment"),Budget("Films")
    
    while True:
        
        menu = input("What do you want to do?\n 1. Set Budget\n 2. Withdraw\n 3. Deposit\n 4. Check Balance of categories \n 5. Check Overall Balance\n 6. Check All Balances\n 7. Add category\n ")
        if menu == "1":
            balance = get_balance()
        if menu == "2":
            choice = get_choice(categories)
            balance = withdraw_deposit(choice,1,balance)
        if menu == "3":
            choice = get_choice(categories)
            balance = withdraw_deposit(choice,0,balance)
        if menu == "4":
             check_balance(categories)
        if menu == "5":
            print("Balance is",balance)
        if menu == "6":
            check_balance(categories)
            print("Overall balance is", balance)
        if menu == "7":
            categories = add_categories(categories)
    
        if menu == "x":
            break


Main()








