#-*- coding: utf-8 -*-
import csv

'''
讀檔
r - 讀取(檔案需存在)
w - 新建檔案寫入(檔案可不存在，若存在則清空)
a - 資料附加到舊檔案後面(游標指在EOF)
r+ - 讀取舊資料並寫入(檔案需存在且游標指在開頭)
w+ - 清空檔案內容，新寫入的東西可在讀出(檔案可不存在，會自行新增)
a+ - 資料附加到舊檔案後面(游標指在EOF)，可讀取資料
b - 二進位模式
'''

f = open('foo.txt', 'r')
print(f.name)
print(f.read())
f.close()

f = open('foo.txt', 'w')
f.write("Hello World\nyou write a data in foo.txt\n")
print('write success')
f.close()


with open('foo.txt', 'r') as fp:
    a = fp.readlines()
    print(f"a: {a}")

with open('foo.txt', 'r') as fp:
    b = fp.read()
    print(f"b: {b}")

with open('foo.txt', 'r') as fp:
    c = fp.readline()
    print(f"c: {c}")

with open('foo.txt', 'a+') as fp:
    fp.write('Hello')
    fp.writelines('hello world')


with open('foo.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')