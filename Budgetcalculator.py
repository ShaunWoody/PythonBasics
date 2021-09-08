class Budget:

    def __init__(self,category,balance = 0):
        self.category = category
        self.balance = balance
    
    def withdraw(self,withdrawamount):
        
        self.balance = self.balance - withdrawamount
  

    def deposit(self,depositamount):

        self.balance = self.balance + depositamount


categories = Budget("Food"),Budget("Entertainment"),Budget("Films")


def get_balance():
    balance = int(input("Enter your budget balance"))
    return balance

balance = get_balance()



def get_choice():
    userchoice1 = input("Enter category or type L to list them: ").lower

    if userchoice1 == "l":
        for s in categories:
            print(s.category)
            
    
    for i in categories:
        if userchoice1 == i.category.lower():
            return i
    else:
        ("Wrong input")
    

def get_deposit_or_withdraw():
    userchoice = input("Enter d or w: ")
    if userchoice == "d":
        return 0
    if userchoice == "w":
        return 1

def withdraw_deposit(choice,depo_or_with,balance):
    
    if depo_or_with == 0:
        h = int(input("Amount to deposit: "))
        choice.deposit(h)
        balance = balance - h
        
    if depo_or_with == 1:
        s = int(input("Amount to withdraw: "))
        choice.withdraw()  
        balance = balance - s
    return balance

while True:
    choice = get_choice()
    dw = get_deposit_or_withdraw()
    balance = withdraw_deposit(choice,dw,balance)
    
    
    print("Food has", categories[0].balance)
    print("Your total balance is:", balance)
    
    if choice == "x":
        break










