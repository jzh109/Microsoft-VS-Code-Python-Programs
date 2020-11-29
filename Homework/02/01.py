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


def main():
    a = int(input())
    if a % 1:
        return -1
    for i in range(2, a // 2 + 1, 1):
        if isprime(i) & isprime(a - i):
            print(i, end=' ')
            print(a - i)


if __name__ == '__main__':
    main()
