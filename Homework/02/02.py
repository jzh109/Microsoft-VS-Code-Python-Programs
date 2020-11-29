def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    a = list(map(int, input().split()))
    temp = int(gcd(a[0], a[1]))
    res = (temp, int(a[0] * a[1] / temp))
    print(res)
    print(type(res))


if __name__ == '__main__':
    main()
