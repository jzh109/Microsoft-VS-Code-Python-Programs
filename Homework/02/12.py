class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate / 100
        self.__monthlyInterestRate = self.__annualInterestRate / 12

    def getId(self):
        return self.__id

    def getbalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return '%f%%' % self.__annualInterestRate

    def getMonthlyInterestRate(self):
        return '%f%%' % self.__monthlyInterestRate

    def getMonthlyInterest(self):
        return self.__balance * self.__monthlyInterestRate

    def withdraw(self, v):
        self.__balance -= v

    def deposit(self, v):
        self.__balance += v

    def setId(self, id):
        self.__id = id

    def setBalance(self, v):
        self.__balance = v

    def setAnnualInterestRate(self, v):
        self.__annualInterestRate = v / 100


def main():
    account = Account('122', 20000, 4.5)
    account.deposit(3000)
    account.withdraw(2500)
    print(account.getId())
    print(account.getbalance())
    print(account.getMonthlyInterestRate())
    print(account.getMonthlyInterest())


if __name__ == '__main__':
    main()
