class BankAccount:
    def __init__(self, username, password ,balance, account_type):
        self._username = username
        self._password = password
        self._current_balance = balance
        self._account_type = account_type

        if account_type == 'SavingsAccount':
            self._min_balance = 5000
            self._interest = 3
            self._withrawable_balance = self._current_balance - self._min_balance
        
        elif account_type == 'OverdraftAccount':
            self._max_balance = self._current_balance
            self._od_limit = 0.1 * self._max_balance
            self._od_fee_percent = 1
            self._interest = 3

        else:
            self._account_type = 'CurrentAccount'


    def deposit(self, amount):
        self._current_balance += amount
        
        if(self._account_type == 'OverdraftAccount'):
            self._max_balance += max(self._max_balance, self._current_balance)
        
        

    def withdraw(self, amount):
        if(self._account_type == 'CurrentAccount'):
            self._current_balance -= amount
        elif(self._account_type == 'SavingsAccount'):
            self._current_balance -= amount
        elif(self._account_type == 'OverdraftAccount'):
            self._current_balance -= amount

        
class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts = {}

    def open_account(self, username, password, balance, account_type):
        new_account = BankAccount(username, password ,balance, account_type)
        self.accounts[username] = new_account
        return new_account

    #def transfer(self, sender_account, amount, password,  receiver_account)


class ATM:
    def __init__(self, bank):
        self.bank = bank
    
    def menu(self):
        print (f"Welcome to {self.bank.name} ATM")

        input_username = input("Enter your username:")
        input_password = input("Enter your password:")

        account = self.bank.accounts.get(input_username)

        if account and account._password == input_password:
            print("Login successfull.")
        else:
            print("Login failed.")
            return
        
        choice = 1

        while choice!=0:

            choice = int(input("\nSelect Option" 
                "\n1. Account Information" 
                "\n2. Check Balance" 
                "\n3. Deposit" 
                "\n4. Withdrawal" 
                "\n4. Transfer Money" 
                "\n Press 0 to exit."
                "\nEnter your choice:"))
            
            if(choice ==0):
                print("Thank you for visiting.")

            if(choice == 1):
                print(f"Username: {account._username}"
                      f"\nAccount Type: {account._account_type}")

                if account._account_type == 'SavingsAccount':
                    print(f"Min Balance: {account._min_balance}"
                          f"\nInterest Rate: {account._interest}")

        
                elif account._account_type == 'OverdraftAccount':
                    print(f"Max Balance: {account._max_balance}"
                          f"\nInterest Rate: {account._interest}"
                          f"\nOd Limit: {account._od_limit}"
                          f"\nOd Fee Percent: {account._od_fee_percent}")

            

            elif(choice == 2):
                print(f"Current Balance: {account._current_balance}")
            

            elif(choice == 3):
                print("Deposit")
                amount = float(input("Enter the deposit amount:"))

                if(amount <= 0):
                    print("Invalid Amount")
                    return 
                
                account.deposit(amount)
                print("Deposit successful."
                      f"\nCurrent Balance: {account._current_balance}")
            

            elif(choice == 4):
                print("Withdrawal")

                if(amount <= 0):
                    print("Invalid Amount")
                    return 
                
                if(amount > account._current_balance):
                    if account._account_type == 'CurrentAccount':
                        account.withdraw(amount)
                        print("Withdrawal successful."
                              f"\nCurrent Balance: {account._current_balance}")

                    elif account._account_type == 'SavingsAccount':
                        if(amount > account._min_balance):
                            account.withdraw(amount)
                            print("Withdrawal successful."
                                  f"\nCurrent Balance: {account._current_balance}")

                    elif account._account_type == 'SavingsAccount':
                        if(self.balance + self._od_limit >= amount):
                            account.withdraw(amount)
                        else:
                            print("Withdrawal unsuccessful. Insufficient balance.")
                            


                else:
                    print("Withdrawal unsuccessful. Insufficient balance.")
                
            elif(choice == 5):
                sender_account = account
                receiver_username = input("Enter receivers username:")
                receiver_account = self.bank.accounts.get(receiver_username)
                amount = int(input("Enter amount to transfer:"))

                if( amount<0 ):
                    print("Invalid amount.")
                

                if(sender_account and receiver_account and amount>account._current_balance):
                    sender_account.withdraw(amount)
                    receiver_account.deposit(amount)
                    print("Transfer successfull")
                else:
                    print("Transfer successfull")
                    
                
                
            else:
                print("Invalid input.")

        

    

icici = Bank('ICICI')

a1 = icici.open_account('Vivek', 'p@ss', 50000, 'SavingsAccount')
a2 = icici.open_account('Sanjay', 'p@ss', 50000, 'OverdraftAccount')
a3 = icici.open_account('Aman', 'p@ss', 50000, 'CurrentAccount')

atm = ATM(icici)

atm.menu()