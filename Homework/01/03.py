def main():
    b = a = input()
    a = list(a)
    b = list(b)
    a.reverse()
    print(str(a) == str(b))


if __name__ == '__main__':
    main()
