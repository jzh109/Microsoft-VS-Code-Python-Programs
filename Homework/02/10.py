def main():
    li = list(map(int, input().split()))
    for i in range(len(li)):
        for j in range(len(li) - 1 - i):
            if li[j] < li[j + 1]:
                li[j + 1], li[j] = li[j], li[j + 1]

    print(li)


if __name__ == '__main__':
    main()
