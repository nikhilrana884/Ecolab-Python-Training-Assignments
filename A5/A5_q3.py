class BankAccount:
    def __init__(self, acc_no, name, password, balance, int_rate):
        self.acc_no = acc_no
        self.name = name
        self.password = password
        self.balance = balance
        self.int_rate = int_rate


    def info(self):
        return(f"Account Number: {self.acc_no}\
                \nName: {self.name}\
                \nBalance: {self.balance}\
                \nInterest Rate: {self.int_rate}\
                \n")
    

    def deposit(self, amount):
        if(amount<0):
            print( "Amount is negative.\n")
            return
        
        self.balance += amount

        print(f"Deposit of {amount} successful.\
                \nCurrent Balance:{self.balance}\n")
    

    def withdraw(self, amount, password):
        if(password!=self.password):
            print("Wrong Password\n")
            return

        if(amount<0):
            print("Amount is negative.\n")
            return
        
        if(amount>self.balance):
            print("Insufficient balance.\n")
            return
        
        self.balance -= amount
        print(f"Withdrawal of {amount} successful.\
                \nCurrent Balance:{self.balance}\n")
    
        
    def credit_interest(self):
        interest = self.balance * self.int_rate / 1200
        self.balance += interest
        print(f"Monthly interest is {interest}.\n")

acc1 = BankAccount("0001", "Test", "test12", 1000, 3)

print(acc1.info())
acc1.deposit(1000)
acc1.deposit(-1000)
acc1.withdraw((500),"test12")
acc1.withdraw((500),"test1")
acc1.credit_interest()