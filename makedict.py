import argparse
import csv
import os.path


DICTFILE = 'DEREMAS.txt'


def make_atok_dict(chars):
    with open(DICTFILE, mode='w', encoding='utf-16', newline='') as dictfile:
        pass
        w = csv.writer(dictfile, dialect=csv.excel_tab)
        w.writerow(['!!ATOK_TANGO_TEXT_HEADER_1'])

        for row in chars:
            kana = row[0].split('　')
            if len(kana) > 1:
                name = row[1].split('　')
                w.writerow([kana[0], name[0],
                           '固有人姓', f'{name[0]}{name[1]}', 'しない', ''])
                w.writerow([kana[1], name[1],
                           '固有人名', f'{name[0]}{name[1]}', 'しない', ''])
                w.writerow([f'{kana[0]}{kana[1]}', f'{name[0]}{name[1]}',
                           '固有人他',
                           f'{row[4]}出身・{row[3]}生まれ・{row[5]}' +
                           (f'（CV：{row[15]}）' if row[15] else ''),
                           'しない', f'CV：{row[15]}' if row[15] else ''])
            else:
                if row[1] == 'トレーナー':
                    altword = '青木明'
                elif row[1] == 'ベテラントレーナー':
                    altword = '青木聖'
                elif row[1] == 'マスタートレーナー':
                    altword = '青木麗'
                elif row[1] == 'ルーキートレーナー':
                    altword = '青木慶'
                else:
                    altword = f'CV：{row[15]}' if row[15] else ''

                if 'とれーなー' in kana[0]:
                    w.writerow([kana[0], row[1],
                               '名詞',
                               f'{row[4]}出身・{row[3]}生まれ・{row[5]}' +
                               f'（CV：{row[15]}）', 'しない',
                               altword, f'CV：{row[15]}'])
                else:
                    w.writerow([kana[0], row[1], '固有人他',
                               f'{row[4]}出身・{row[3]}生まれ・{row[5]}' +
                               (f'（CV：{row[15]}）' if row[15] else ''),
                               'しない', altword])


def make_macos_dict(chars):
    with open(DICTFILE, mode='w', encoding='utf-16', newline='') as dictfile:
        w = csv.writer(dictfile, quoting=csv.QUOTE_ALL)

        for row in chars:
            kana = row[0].split('　')
            if len(kana) > 1:
                name = row[1].split('　')
                w.writerow([f'{kana[0]}', f'{name[0]}', '人名'])
                w.writerow([f'{kana[1]}', f'{name[1]}', '人名'])
                w.writerow([f'{kana[0]}{kana[1]}',
                            f'{name[0]}{name[1]}', '人名'])
            else:
                if 'とれーなー' in kana[0]:
                    w.writerow([f'{kana[0]}', f'{row[1]}', '普通名詞'])
                else:
                    w.writerow([f'{kana[0]}', f'{row[1]}', '人名'])


def make_msime_dict(chars):
    with open(DICTFILE, mode='w', encoding='utf-16', newline='') as dictfile:
        w = csv.writer(dictfile, dialect=csv.excel_tab)

        for row in chars:
            kana = row[0].split('　')
            if len(kana) > 1:
                name = row[1].split('　')
                w.writerow([kana[0], name[0], '姓'])
                w.writerow([kana[1], name[1], '名'])
                w.writerow([f'{kana[0]}{kana[1]}', f'{name[0]}{name[1]}', '人名',
                           f'{row[4]}出身・{row[3]}生まれ・{row[5]}' +
                           (f'（CV：{row[15]}）' if row[15] else '')])
            else:
                if 'とれーなー' in kana[0]:
                    w.writerow([kana[0], row[1], '名詞',
                               f'{row[4]}出身・{row[3]}生まれ・{row[5]}' +
                               f'（CV：{row[15]}）'])
                else:
                    w.writerow([kana[0], row[1], '人名',
                               f'{row[4]}出身・{row[3]}生まれ・{row[5]}' +
                               (f'（CV：{row[15]}）' if row[15] else '')])


def read_chars() -> list:
    with open(os.path.abspath('characters.txt'), encoding='utf-8') as datafile:
        r = csv.reader(datafile)

        # skip the header row
        next(r)

        return [row for row in r]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ime', choices=['atok', 'macos', 'msime'])

    args = parser.parse_args()

    chars = read_chars()

    if args.ime == 'atok':
        make_atok_dict(chars)
    elif args.ime == 'macos':
        make_macos_dict(chars)
    elif args.ime == 'msime':
        make_msime_dict(chars)


if __name__ == '__main__':
    main()
