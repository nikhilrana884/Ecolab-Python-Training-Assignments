class BankAccount:
    def __init__(self, username, password ,balance, account_type):
        self._username = username
        self._password = password
        self._current_balance = balance
        self._account_type = account_type

        if account_type == 'Savings':
            self._min_balance = 5000
            self._interest = 3
        
        elif account_type == 'OverdraftAccount':
            self._max_balance = self._current_balance
            self._od_limit = 0.1 * self._max_balance
            self._od_fee_percent = 1

    def deposit(self):
        pass

    def withdraw(self):
        pass



        
class Bank:
    def __init__(self,name):
        self._name = name
        self.accounts = []

    def open_account(self, username, password, balance, account_type):
        pass

    def transfer(self, sender_username, amount, password, receiver_username):
        pass


class ATM:
    pass   
    

sbi = Bank('SBI')
print(sbi._name)
