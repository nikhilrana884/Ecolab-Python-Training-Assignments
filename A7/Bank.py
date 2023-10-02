class BankAccount:
    def __init__(self, username, password ,balance, account_type):
        self._username = username
        self._password = password
        self._current_balance = balance
        self._account_type = account_type

        if account_type == 'SavingsAccount':
            self._min_balance = 5000
            self._interest = 3
        
        elif account_type == 'OverdraftAccount':
            self._max_balance = self._current_balance
            self._od_limit = 0.1 * self._max_balance
            self._od_fee_percent = 1


    def deposit(self, amount):
        if(amount > 0):
            self._current_balance += amount
        else:
            print("Invalid Amount")
        
        if(self._account_type == 'OverdraftAccount'):
            self._max_balance += max(self._max_balance, self._current_balance)
        
        

    def withdraw(self):
        pass



        
class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts = {}

    def open_account(self, username, password, balance, account_type):
        new_account = BankAccount(username, password ,balance, account_type)
        self.accounts[username] = new_account
        return new_account

    def transfer(self, sender_username, amount, password, receiver_username):
        pass


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
        
        choice = int(input("\nSelect Option" 
              "\n1. Account Information" 
              "\n2. Check Balance" 
              "\n3. Deposit" 
              "\n4. Withdrawal" 
              "\nEnter your choice:"))

        if(choice == 1):
            print(f"Username: {account._username}")
            print(f"Account Type: {account._account_type}")

        elif(choice == 2):
            print(f"Current Balance: {account._current_balance}")
        
        elif(choice == 3):
            amount = float(input("Enter the deposit amount:"))
            account.deposit(amount)
            if(amount < 0):
                print("Invalid Amount")
                return 
            
            print("Deposit successful.")
            print(f"Current Balance: {account._current_balance}")
        
        elif(choice == 4):
            print("Withdrawal")

        else:
            print("Invalid input.")

        

    

icici = Bank('ICICI')

a1 = icici.open_account('Vivek', 'p@ss', 50000, 'SavingsAccount')
a2 = icici.open_account('Sanjay', 'p@ss', 50000, 'OverdraftAccount')
 
atm = ATM(icici)

atm.menu()