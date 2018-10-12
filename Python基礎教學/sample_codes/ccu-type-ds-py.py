#-*- coding:utf-8 -*-
# reference: https://realpython.com/python-lists-tuples/
# try: https://realpython.com/quizzes/python-lists-tuples/
# https://realpython.com/python-strings/
# try: https://realpython.com/quizzes/python-data-types/
import sys

print(sys.version)

"""
基本資料型態: int, float, str, bytes, ord, 
基本資料結構: list, dict, set, tuple
"""
# int, float, str
x = 2
x += 1
x -= 1
print(type(x), x)
x = float(x)
print(type(x), x)

x, y = 10.0, 5
print(f'{type(x)} x={x}, {type(y)} y={y}')

x = 'Hello'
x += ',World'  # x = x + ' World'
print(type(x), x)
x1 = x.replace(',', ' ')
print(x1)

w = '台灣'
print(type(w), w)

w1 = w.encode('utf-8')
print(type(w1), w1)
print(type(w1.decode('utf-8')), w1.decode('utf-8'))

w = w.encode('big5')
print(type(w), w, w.decode('big5'))

w = u'台灣'
print(type(w), w, repr(w))

a = 'a'
A = 'A'
print(a, ord(a), A, ord(A))


# list
lists = []
lists.append(1)
print(lists)
lists.append(2)
print(lists)

lists = list()
lists.append(1)
print(lists)

a = 'a'
lists = [10.0, 'Hello World', a, [1,2,3]]
print(lists)
print(lists[0], lists[-1])

lists.pop()
print(lists)

lists.insert(0, 20.0)
print(lists)

lists.remove(10.0)
print(lists)

print(lists.index(20.0))

list_a = ['Hello']
list_b = ['World']
list_a.extend(list_b)
print(list_a)

list_a.clear()
print(list_a)

lists = [5, 4, 2, 0, 3, 1]
lists.sort()
print(lists)

for i in lists:
    print(i)

lists.reverse()
print(lists)

lists = ['this is a', 'this is b']

a, b = lists
print(a)
print(b)


lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lists[0::1])
print(lists[0::2])
print(lists[0::3])
print(lists[0:])
print(lists[3:])
print(lists[-1])

print(lists[::-1]) #lists.reverse()
print(lists[0:-10])


# list adv

#Lists are ordered.
a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']
print(a == b)
print(a is b)

#Lists can contain any arbitrary objects.
a = [2, 4, 6, 8]
print(a)
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a)

def foo():
    pass

import math

a = [int, len, foo, math]
print(a)

# 不用唯一，可以放任何數（假如你記憶體允許）
a = ['bark', 'meow', 'woof', 'bark', 'cheep', 'bark']
print(a)

#List elements can be accessed by index.
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0])
print(a[2])
print(a[5])

# 切片 Slice
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[2:5])
print(a[-5:-2])
print(a[1:4])
print(a[-5:-2] == a[1:4])


# 省略切片第一個索引就是從頭開始
print(a[:4], a[0:4])
print(a[2:], a[2:len(a)])

print(a[:4] + a[4:])
print(a[:4] + a[4:] == a)


# 指定步幅
print(a[0:6:2])
print(a[1:6:2])
print(a[6:0:-2])

# 反轉
print(a[::-1])

# [:] list 與 string 差異, 對 list 而言 [:] 是 copy
s = 'foobar'
print(s[:])
print(s[:] is s)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[:])
print(a[:] is a)

# in, not 操作
print('qux' in a)
print('thud' not in a)

# concatenation(+), replication(*)
print(a + ['grault', 'garply'])
print(a * 2)

# len(), min(), max()
print(len(a))
print(min(a))
print(max(a))

# 直接對 string 操作
print('If Comrade Napoleon says it, it must be right.'[::-1])


#Lists can be nested to arbitrary depth.
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x)
print(x[0], x[2], x[4])
print(x[1])
print(x[3])

print(x[1][0])
print(x[1][1])
print(x[1][2])
print(x[1][3])

print(x[3][0])
print(x[3][1])

print(x[1][1])
print(x[1][1][0], x[1][1][1])

print(x[1][1][-1])
print(x[1][1:3])
print(x[3][::-1])

print(len(x))

print('ddd' in x)
print('ddd' in x[1])
print('ddd' in x[1][1])

#Lists are mutable.


#Lists are dynamic



# dict
stores = {'apple': 10, 'cake': 5}
print(stores)
stores['orange'] = 10
print(stores)
stores.setdefault('juice', 12)
print(stores)
stores.setdefault('apple', 12)
print(stores)
stores['apple'] = 12
print(stores)

print(stores['apple'])
print(stores.get('apple'))

stores.pop('apple')
print(stores)
stores['apple'] = 12
print(stores)

stores.update({'beer': 20, 'win': 2})
print(stores)

del stores['apple']
print(stores)

print(stores.keys())
print(stores.values())

for k, v in stores.items():
    print(k, '-->', v)

user = {'Tom': ['M','16'], 'Mary': ['Female', '17']}
print(user)


# set
admins = set()
users = {'Smile', 'Tony','Happy','Sherry','Allen','Andy', 'Mars'}
print(type(users), users)
admins.add('ihc')
admins.add('Mars')

print(admins & users)
print(admins | users)
print(admins ^ users)
print(admins - users)
print(users - admins)


# list v.s str
strs = 'helloworld'
print(strs[0:5])
strs = list(strs)
print(strs)
strs = ''.join(strs)
print(strs)



