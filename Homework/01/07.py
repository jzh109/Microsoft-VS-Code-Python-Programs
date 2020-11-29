def main():
    options = {}
    q = input()
    temp = list(q.split(' '))
    q = str()
    for i in temp:
        if i == '____':
            if i is temp[0]:
                q += '{}'
            else:
                q += ' {}'
        else:
            q += ' ' + i

    for i in range(2):
        a = input()
        options[a.split('.')[0]] = a.split('.')[1].strip()
    a = input()
    print(q.format(options.get(a[0]), options.get(a[1])))


if __name__ == '__main__':
    main()
