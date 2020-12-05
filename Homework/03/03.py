from xlwt import Workbook, Font, XFStyle, Alignment


def main():
    lst = []
    path = r'./Homework/03/'

    with open(path + 'test.txt', 'r') as fpin:
        title = fpin.readline().strip().replace('\n', '').split(',')
        while True:
            s = fpin.readline().strip().replace('\n', '').split(',')
            if s == ['']:
                break
            lst.append(s)
    fpin.close()

    book = Workbook()
    sheet1 = book.add_sheet('data')

    style = XFStyle()

    font = Font()
    font.name = '宋体'
    font.height = 280
    style.font = font

    alignment = Alignment()
    alignment.horz = Alignment.HORZ_CENTER
    alignment.vert = Alignment.VERT_CENTER
    style.alignment = alignment

    row = sheet1.row(0)
    for i, j in zip(range(len(title)), title):
        row.write(i, j, style=style)
    for i, j in zip(range(1, len(lst) + 1), lst):
        row = sheet1.row(i)
        for x, y in zip(range(len(j)), j):
            row.write(x, y, style=style)
    book.save(path + 'data.xls')


if __name__ == '__main__':
    main()
