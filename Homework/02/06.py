import random


def main():
    a = random.randint(0, 100)
    for i in range(5):
        guess = int(input())
        if guess == a:
            print("你猜对了。")
            break
        elif guess > a:
            print("大了")
        else:
            print("小了")


if __name__ == '__main__':
    main()
