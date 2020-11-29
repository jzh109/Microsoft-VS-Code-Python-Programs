def main():
    origin = input()
    userinput = input()
    res = 0
    for i in range(len(origin)):
        if origin[i] == userinput[i]:
            res += 1
    print(res / len(userinput))


if __name__ == '__main__':
    main()
