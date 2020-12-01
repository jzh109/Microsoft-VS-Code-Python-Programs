class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate / 100
        self.__monthlyInterestRate = self.__annualInterestRate / 12

    def getId(self) -> int:
        return self.__id

    def getBalance(self) -> float:
        return self.__balance

    def getAnnualInterestRate(self) -> str:
        return '%f%%' % self.__annualInterestRate

    def getMonthlyInterestRate(self) -> str:
        return '%f%%' % self.__monthlyInterestRate

    def getMonthlyInterest(self) -> float:
        return self.__balance * self.__monthlyInterestRate

    def withdraw(self, v: float) -> None:
        self.__balance -= v

    def deposit(self, v: float) -> None:
        self.__balance += v

    def setId(self, id: int) -> None:
        self.__id = id

    def setBalance(self, v: float) -> None:
        self.__balance = v

    def setAnnualInterestRate(self, v: float) -> None:
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
