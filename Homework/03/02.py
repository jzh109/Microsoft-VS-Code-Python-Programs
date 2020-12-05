import string


def main():
    password = input()
    level = 0
    sign = num = low = up = False
    dic = {
        '0': "Unsafe at all",
        '1': "Unsafe",
        '2': "Middle to unsafe",
        '3': "Middle to safe",
        '4': "Safe",
        '5': "Very safe"
    }
    if len(password) >= 8:
        level += 1
    for i in password:
        if (not low) & (i in string.ascii_lowercase):
            level += 1
            low = True
            continue
        if (not up) & (i in string.ascii_uppercase):
            level += 1
            up = True
            continue
        if (not sign) & (i in string.punctuation):
            level += 1
            sign = True
            continue
        if (not num) & (i in string.digits):
            level += 1
            num = True

    print(dic[str(level)])


if __name__ == '__main__':
    main()
