#-*- coding: utf-8 -*-

"""
基本資料型態: int, float, str, bytes, ord, 
基本資料結構: list, dict, set
"""
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
