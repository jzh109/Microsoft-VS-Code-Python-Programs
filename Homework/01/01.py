def main():
    a = input().split(':')[1]
    b = input().split(':')[1]
    c = input().split(':')[1]

    f = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'Noveber',
        '12': 'Deceber'
    }

    if c == '01':
        c += 'st'
    elif c == '02':
        c += 'nd'
    elif c == '03':
        c += 'rd'
    else:
        c += 'th'
    print(f[b] + ' ' + c + ', ' + a)


if __name__ == '__main__':
    main()
