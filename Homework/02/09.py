def main():
    li = list(map(int, input().split()))
    a = []
    li.sort()
    a.append(li[len(li) - 1])
    a.append(li[0])
    a = tuple(a)
    print(a)


if __name__ == '__main__':
    main()
