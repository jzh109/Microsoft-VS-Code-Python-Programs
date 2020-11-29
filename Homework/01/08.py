import random


def main():
    try:
        while True:
            n = int(input())
            a = set()
            for i in range(n):
                a.add(random.randint(1, 1001))
            a = list(a)
            a.sort()
            print(a)
    except EOFError:
        pass


if __name__ == '__main__':
    main()
