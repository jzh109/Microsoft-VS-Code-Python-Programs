import re


def main():
    a = re.findall('[0-9-]+', input().strip())
    print(a)


if __name__ == '__main__':
    main()
