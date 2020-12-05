import jieba


def main():
    s = ''
    try:
        while True:
            s += input()
    except EOFError:
        pass
    punctuation = '，。、；’【】-=·！@#￥%……&*（）——+{}|、“：？》《 '
    for i in punctuation:
        s = s.replace(i, '')
    lst = list(jieba.cut(s))
    dic = {}
    for i in lst:
        if dic.get(i) is None:
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)


if __name__ == '__main__':
    main()
