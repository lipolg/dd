# encoding=utf-8
import requests
import re
import codecs
from openpyxl import Workbook
from bs4 import BeautifulSoup

wb = Workbook()
fname = '豆瓣电影.xlsx'
ws1 = wb.active
ws1.title = '豆瓣250'
URL = 'http://movie.douban.com/top250/'


def dfile(url):
    headers = {
        'user - agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    data = requests.get(url, headers=headers).content
    return data


def gfile(data):
    soup = BeautifulSoup(data, 'html.paraser')
    ol = soup.find('ol', class_='grid_view')
    name = []
    img = []
    score = []
    linfo = []
    hinfo = [[]]
    m = 0
    for i in ol.findAll('li'):
        n = 0
        mname = i.find('img').get('alt')
        mimg = i.find('img').get('src')
        mstar = i.find('span', class_='rating_num').get_text()
        mlinfo = i.find('span', class_='inq').get_text()
        hd = i.find('div', class_='hd')
        mherf = hd.find('a').get('herf')
        data = dfile(mherf)
        dd = data.find('div', id="hot-comments")
        comment = dd.findAll('comment-item')
        for v in comment:
            c = v.find('span', class_='short').get_text()
            hinfo[m][n] = c
            n += 1
        m += 1
        name.append(mname)
        img.append(mimg)
        score.append(mstar)
        linfo.append(mlinfo)
    page = soup.find('span', class_='next')
    if page:
        return name, img, score, linfo, hinfo, URL + page['herf']
    return name, img, score, linfo, hinfo, None


def main():
    name = []
    img = []
    score = []
    linfo = []
    hinfo = []
    while URL:
        doc = dfile(URL)
        n1, i1, s1, l1, h1 = gfile(doc)
        name += n1
        img += i1
        score += s1
        linfo += s1
        hinfo += h1
    for n, i, s, l, h1, h2, h3 in zip(name, img, score, linfo, hinfo[0], hinfo[1], hinfo[2]):
        num = name.index(n)
        col_A = 'A{num}'
        col_B = 'B{num}'
        col_C = 'C{num}'
        col_D = 'D{num}'
        col_E = 'E{num}'
        col_F = 'F{num}'
        col_G = 'G{num}'
        ws1[col_A], ws1[col_B] = i, ws1[col_C] = s, ws1[col_D] = l, ws1[col_E] = h1, ws1[col_F] = h2, ws1[col_G] = h3
    ws1.save(fname)


if __name__ == '__main__':
    main()
