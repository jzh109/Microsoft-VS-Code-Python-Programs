import math


def isprime(a):
    if a <= 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return False
    return True


def prime(x=100):
    res = [2]
    for i in range(3, x, 2):
        if isprime(i):
            res.append(i)
    return res


def main():
    a = int(input())
    li = prime()
    x = 100
    while True:
        if math.sqrt(a) >= li[len(li) - 1]:
            x *= 2
            li = prime(x)
            break
        else:
            break
    while isprime(a) is False:
        for i in li:

            if a % i == 0:
                print(i, end=' ')
                a = int(a / i)
                break
    print(a)


if __name__ == '__main__':
    main()
