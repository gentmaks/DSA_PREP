class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, account, money):
        if account < 1 or account > len(self.balance):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account, money):
        if account < 1 or account > len(self.balance) or money > self.balance[account-1]:
            return False
        self.balance[account-1] -= money
        return True

    def transfer(self, account1, account2, money):
        if account1 < 1 or account1 > len(self.balance):
            return False
        if account2 < 1 or account2 > len(self.balance):
            return False
        if money > self.balance[account1-1]:
            return False
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def __str__(self):
        sb = ["\n"]
        for i, b in enumerate(balance):
            sb.append(f"Account {i + 1}, has balance: {balance[i]}")
        return "\n".join(sb)
