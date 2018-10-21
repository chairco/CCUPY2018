#-*- coding: utf-8 -*-
import requests
import urllib

from requests_html import HTML


domain = 'https://www.ptt.cc/'
url = 'https://www.ptt.cc/bbs/joke/index.html'


#讓文字居中，就要計算字符的寬度，然後設置偏移量，在網上搜索得到如下方法
widths = [
        (126,    1), (159,    0), (687,     1), (710,   0), (711,   1),
        (727,    0), (733,    1), (879,     0), (1154,  1), (1161,  0),
        (4347,   1), (4447,   2), (7467,    1), (7521,  0), (8369,  1),
        (8426,   0), (9000,   1), (9002,    2), (11021, 1), (12350, 2),
        (12351,  1), (12438,  2), (12442,   0), (19893, 2), (19967, 1),
        (55203,  2), (63743,  1), (64106,   2), (65039, 1), (65059, 0),
        (65131,  2), (65279,  1), (65376,   2), (65500, 1), (65510, 2),
        (120831, 1), (262141, 2), (1114109, 1),
]


def calc_len(string):
    def chr_width(o):
        global widths
        if o == 0xe or o == 0xf:
            return 0
        for num, wid in widths:
            if o <= num:
                return wid
        return 1
    return sum(chr_width(ord(c)) for c in string)


def pretty_print(push, title, date, author):
    pattern = '%3s\t%s%s%s\t%s'
    padding = ' ' * (50 - calc_len(title))
    print(pattern % (push, title, padding, date, author))


def parser_next_page(resp):
    html = HTML(html=resp.text)
    pages = html.find('.action-bar a.btn.wide')
    link = pages[1].attrs.get('href')
    next_page = urllib.parse.urljoin(domain, link)
    return next_page


def fetch(url):
    response = requests.get(url)
    return response


def parser_article_meta(entry):
    context = {
        'title': entry.find('div.title', first=True).text,
        'push': entry.find('div.nrec', first=True).text,
        'date': entry.find('div.date', first=True).text,
        'author': entry.find('div.author', first=True).text,
    }
    return context


def get_page_meta(resp):
    html = HTML(html=resp.text)
    post_entries = html.find('div.r-ent')

    for entry in post_entries:
        meta = parser_article_meta(entry)
        pretty_print(meta['push'], meta['title'], meta['date'], meta['author'])
        
        
def main(url, nums=1):
    for _ in range(nums):
        resp = fetch(url)
        if resp.status_code == 200:
            get_page_meta(resp)
            url = parser_next_page(resp)
        else:
            print(resp.status_code)


if __name__ == '__main__':
    main(url=url, nums=2)