def main():
    a = list(input())
    a.reverse()
    a = ''.join(a)
    b = set(a)
    for i in range(0, len(a), 1):
        if a[i] in b:
            print(a[i], end='')
            b.remove(a[i])


if __name__ == '__main__':
    main()
