class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            print("You cannot withdraw this amount, since you dont have enough funds")
        elif amount_to_withdraw<=self.balance:
            print(f"You withdrew ${amount_to_withdraw}now.")
            self.balance-=amount_to_withdraw
            print(f"Your balance now is ${self.balance}")
    
    def deposit(self, amount_to_deposit):
        self.balance += amount_to_deposit
        print(f"You successfully deposited ${amount_to_deposit}")
        print(f"Your balance now is ${self.balance}")

    def check_balance(self):
        print(f"Your balance is ${self.balance}")
        return self.balance
    

initial_balance = int(input("""Welcome to our bank
                            
                            Input your initial balance: """))   

acct  = BankAccount(initial_balance) 
print("Your account successfully created")
acct.check_balance()

print("To withdraw press 1, press 2 for deposit")
user_choice = input()
if user_choice == "1":
    withdraw_amt = int(input("Enter amount you want to withdraw"))
    acct.withdraw(withdraw_amt)
elif user_choice == "2":
    deposit_amt = int(input("Enter amount you want to deposit"))
    acct.deposit(deposit_amt)
else:
    print("Invalid option")    


