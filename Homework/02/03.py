def main():
    x = list(map(int, input().split()))
    n = int(input())
    x.sort()
    for i in range(len(x)):
        index = int(i)
        if (int(x[index]) < n) & (int(x[index + 1]) > n):
            x.insert(index + 1, n)
            break
    print(x)


if __name__ == '__main__':
    main()
