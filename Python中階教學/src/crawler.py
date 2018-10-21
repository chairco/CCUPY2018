#-*- coding: utf-8 -*-
import requests

from requests_html import HTML


url = 'https://www.ptt.cc/bbs/joke/index.html'


def fetch(url):
    """
    :param url: string, url
    :ret: response: object requests
    """
    response = requests.get(url)
    return response


def parser_article_meta(entry):
    """
    :param entry: object, each entry
    :ret: pagen context with dict type
    """
    return {
        'title': entry.find('div.title', first=True).text,
        'push': entry.find('div.nrec', first=True).text,
        'date': entry.find('div.date', first=True).text,
        'author': entry.find('div.author', first=True).text,
        #'link': entry.find('div.title > a', first=True).attrs['href'],
    }


def main():
    resp = fetch(url=url)
    if resp.status_code == 200:
        html = HTML(html=resp.text)
        post_entries = html.find('div.r-ent')

        for entry in post_entries:
            meta = parser_article_meta(entry)
            print(meta)
    else:
        print(resp.status_code)


if __name__ == '__main__':
    main()
