import enum


class SPEED(enum.Enum):
    SLOW = 1
    MEDIUM = 2
    FAST = 3


class Fan:
    def __init__(self,
                 color='blue',
                 radius=5.0,
                 on=False,
                 speed=SPEED.SLOW.value):
        self.__color = color
        self.__radius = radius
        self.__on = on
        self.__speed = speed

    def setOn(self, v):
        self.__on = v

    def setColor(self, v):
        self.__color = v

    def setSpeed(self, v):
        self.__speed = v

    def setRadius(self, v):
        self.__radius = v

    def getColor(self):
        return self.__color

    def getOn(self):
        return self.__on

    def getRadius(self):
        return self.__radius

    def getSpeed(self):
        return self.__speed


def main():
    fan1 = Fan('yellow', 10, True, SPEED.FAST.value)
    fan2 = Fan()
    fan2.setColor('blue')
    fan2.setOn(False)
    fan2.setRadius(5)
    fan2.setSpeed(SPEED.MEDIUM.value)

    print(fan1.getColor(), end=' ')
    print(fan1.getOn(), end=' ')
    print(fan1.getRadius(), end=' ')
    print(fan1.getSpeed())

    print(fan2.getColor(), end=' ')
    print(fan2.getOn(), end=' ')
    print(fan2.getRadius(), end=' ')
    print(fan2.getSpeed())


if __name__ == '__main__':
    main()
