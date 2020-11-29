def main():
    a = list(input().split(' '))
    neg = sumall = 0
    for i in range(len(a)):
        temp = int(a[i])
        if temp < 0:
            neg += 1
        else:
            sumall += temp
    print('负数的个数是：' + str(neg))
    print('非负数均值是：' + str((sumall / (len(a) - neg))))


if __name__ == '__main__':
    main()
