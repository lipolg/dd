# encoding=utf8

import os


def cfile(ldir):
    farr = ldir.split("\\")
    num = 1
    print(ldir)
    if os.path.exists(ldir):
        for f in os.listdir(ldir):
            arr = f.split('.')
            os.rename(os.path.join(ldir, f), os.path.join(ldir, farr[-1] + f'{num}.' + arr[1]))
            num += 1
    else:
        return '目录不存在！'


if __name__ == '__main__':

    cfile(r'D:\美剧\性教育')
