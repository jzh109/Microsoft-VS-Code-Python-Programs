class Stock:
    def __init__(self, symbol: str, name: str, previousClosingPrice: float,
                 currentPrice: float):
        self.__stockSymbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    @property
    def getsymbol(self) -> str:
        return self.__stockSymbol

    @property
    def getname(self) -> str:
        return self.__name

    def getPreviousClosingPrice(self) -> float:
        return self.__previousClosingPrice

    def getCurrentPrice(self) -> float:
        return self.__currentPrice

    def getChangePercent(self) -> str:
        s = (self.__previousClosingPrice -
             self.__currentPrice) / self.__currentPrice
        s = '{0:%}'.format(s)
        return s

    def setPreviousClosingPrice(self, v: float) -> None:
        self.__previousClosingPrice = v

    def setCurrentPrice(self, v: float) -> None:
        self.__currentPrice = v


def main():
    stock = Stock('INTC', 'Intel Corporation', 20.5, 20.35)
    print(stock.getsymbol)
    print(stock.getname)
    print(stock.getPreviousClosingPrice())
    print(stock.getCurrentPrice())
    print(stock.getChangePercent())


if __name__ == '__main__':
    main()
