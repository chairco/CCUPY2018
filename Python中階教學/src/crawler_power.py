#-*- coding: utf-8 -*-
import re

import requests
import urllib

from requests_html import HTML


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


def pretty_print_board(index, name, cla, title):
    pattern = '%3s\t%s%s%s\t%s'
    padding = ' ' * (50 - calc_len(title))
    print(pattern % (index, name, padding, title, cla))


class PTT:

    def __init__(self):
        self.domain = 'https://www.ptt.cc/'

    def fetch(self, url):
        response = requests.get(url=url, cookies={'over18': '1'})
        return response

    def parser_next_page(self, resp):
        html = HTML(html=resp.text)
        pages = html.find('.action-bar a.btn.wide')
        link = pages[1].attrs.get('href')
        next_page = urllib.parse.urljoin(self.domain, link)
        return next_page

    def parser_article_meta(self, entry):
        context = {
            'title': entry.find('div.title', first=True).text,
            'push': entry.find('div.nrec', first=True).text,
            'date': entry.find('div.date', first=True).text,
            'author': entry.find('div.author', first=True).text,
        }

        try:
            context['link'] = entry.find('div.title > a', first=True).attrs['href']
        except AttributeError:
            if '(本文已被刪除)' in context['title']:
                match_author = re.search('\[(\w*)\]', context['title'])
                if match_author:
                    context['author'] = match_author.group(1)
            elif re.search('已被\w*刪除', context['title']):
                match_author = re.search('\<(\w*)\>', context['title'])
                if match_author:
                    context['author'] = match_author.group(1)
        
        return context

    def parser_boardlist_meta(self, entry):
        context = {
            'name': entry.find('div.board-name', first=True).text,
            'nuser': entry.find('div.board-nuser', first=True).text,
            'class': entry.find('div.board-class', first=True).text,
            'title': entry.find('div.board-title', first=True).text,
        }
        return context

    def get_page_meta(self, resp):
        html = HTML(html=resp.text)
        post_entries = html.find('div.r-ent')

        for entry in post_entries:
            meta = self.parser_article_meta(entry)
            pretty_print(meta['push'], meta['title'],
                         meta['date'], meta['author'])

    def get_board_list(self, resp):
        boards = []
        html = HTML(html=resp.text)
        board_entries = html.find('div.b-ent')

        for idx, entry in enumerate(board_entries):
            meta = self.parser_boardlist_meta(entry)
            pretty_print_board(idx, meta['name'], meta['class'], meta['title'])
            boards.append(meta['name'])

        return boards


def main(url, nums=1):
    """
    Flow: 
        show board list -> 
          input select board and how page deep crawler
    """
    ptt = PTT()
    resp = ptt.fetch(url=url)
    if resp.status_code == 200:
        boards = ptt.get_board_list(resp)
    else:
        print(f"Connect {url} Fail, {resp.status_code}")
        return

    while True:
        index = input('輸入看板序號, 輸入 exit 離開:\n')
        if isinstance(index, str):
            if index == 'exit':
                print('bye bye')
                break

        if 0 <= int(index) <= len(boards):
            board = boards[int(index)]
            nums = int(input(f'選擇: {board}, 輸入爬取深度:\n'))
            board_url = urllib.parse.urljoin(url, board)

            for _ in range(nums):
                resp = ptt.fetch(url=board_url)
                if resp.status_code == 200:
                    ptt.get_page_meta(resp)
                    board_url = ptt.parser_next_page(resp)
                else:
                    print(resp.status_code)
                    break
                print(f"{'-'*50}\t")
            break
        else:
            print(index)


if __name__ == '__main__':
    main(url='https://www.ptt.cc/bbs/')
