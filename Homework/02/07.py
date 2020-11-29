def main():
    a = input()
    li = []
    res = 0
    for i in range(int(a)):
        s = a
        for j in range(i):
            s += a
        li.append(int(s))
    for i in li:
        res += i
    print(res)


if __name__ == '__main__':
    main()
