#-*- coding: utf-8 -*-
# Quick Python Script Explanation for Programmers
import os


def main():
    print('Hello World!')

    print('這是來自 Alice\'s 的問候')
    print('這是來自 Bob\' 的問候')

    foo(5, 10)

    print('=' * 10)
    print('這將執行' + os.getcwd())

    counter = 0
    counter += 1

    foods = ['apples', 'orange', 'cats']
    for food in foods:
        print(f'我喜歡吃 {food}')

    print('數到 10')
    for i in range(10):
        print(i)


def foo(paraml, secondParam):
    """這個是
    多行的註釋
    """
    res = paraml + secondParam

    print('%s 加 %s 等於 %s' % (paraml, secondParam, res))
    print('{} 加 {} 等於 {}'.format(paraml, secondParam, res))
    print(f'{paraml} 加 {secondParam} 等於 {res}')

    if res < 50:
        print('這個')
    elif res >= 50 and paraml == 45 or secondParam == 24:
        print('那個')
    else:
        print('嗯...')

    return res

if __name__ == '__main__':
    main()
