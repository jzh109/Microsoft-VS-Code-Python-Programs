def main():
    n = int(input())
    for i in range(1, n + 1, 1):
        for j in range(1, n + 1, 1):
            if i in [1, int((n + 1) / 2), n]:
                if j in [1, int((n + 1) / 2), n]:
                    print('+ ', end='')
                    if j == n:
                        print()
                else:
                    print('- ', end='')
            elif j in [1, int((n + 1) / 2), n]:
                print('| ', end='')
                if j == n:
                    print()
            else:
                print('  ', end='')


if __name__ == '__main__':
    main()
