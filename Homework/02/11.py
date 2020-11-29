class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__stockSymbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    @property
    def getsymbol(self):
        return self.__stockSymbol

    @property
    def getname(self):
        return self.__name

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def getChangePercent(self):
        s = (self.__previousClosingPrice -
             self.__currentPrice) / self.__currentPrice
        s = '{0:%}'.format(s)
        return s

    def setPreviousClosingPrice(self, v):
        self.__previousClosingPrice = v

    def setCurrentPrice(self, v):
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
