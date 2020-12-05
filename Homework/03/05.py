import re


def main():
    print(re.split(r', |(?= (?:\d{5}|[A-Z]{2})) ', input()))


if __name__ == '__main__':
    main()
