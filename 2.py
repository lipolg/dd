# encoding=utf8

import os


def cfile(ldir):
    num = 1
    s = 1
    farr = ldir.split("\\") #获取文件名
    if os.path.exists(ldir):
        for f in os.listdir(ldir):
            if os.path.isdir(os.path.join(ldir, f)):
                fname = farr[-1] + f'第{s}季'
                os.rename(os.path.join(ldir, f), os.path.join(ldir, fname)) #重命名文件夹
                cfile(os.path.join(ldir, fname))
                s += 1
            else:
                arr = f.split('.')  #取后缀
                os.rename(os.path.join(ldir, f), os.path.join(ldir, farr[-1] + f'第{num}集.' + arr[1]))   #重命名文件
                num += 1
    else:
        return '目录不存在！'


if __name__ == '__main__':
    cfile(r'D:\美剧\老爸老妈的浪漫史')
