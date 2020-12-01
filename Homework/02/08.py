def main():
    temp = list(map(int, input().split()))
    n = temp[0]
    k = temp[1] - 1
    point = 0
    li = []
    for i in range(1, n + 1):
        li.append(i)
    while len(li) > 1:
        point = (point + k) % n
        del li[point]
        n -= 1
    print(li[0])


if __name__ == '__main__':
    main()
