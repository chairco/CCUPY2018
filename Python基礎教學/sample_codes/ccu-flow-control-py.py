#-*- coding: utf-8 -*-

"""
流程控制與條件判斷
"""

my_list = []
for i in range(0, 10):
    my_list.append(i)

print(my_list)


for i in range(2, 10):
    print(i)
    for j in range(1, 10):
        print(f"{i}*{j}={i*j}")


if my_list[0] == 1:
    my_list[0] += 1
    print('list[0] add 1')
else:
    my_list[0] += 2
    print('list[0] add 2')

print(my_list)


if 9 in my_list:
    print('my_list has 9')


if 9 in my_list and 0 in my_list:
    print('9 and 0 in my_list')
elif 9 in my_list or 0 in my_list:
    print('9 or 0 in my_list')
else:
    print('9 and 0 not in my_list')


score = 80

if 70 <= score <= 90:
    print('score between 70~90')

if 90 >= score >= 70:
    print('score between 70~90')


c = 0
while True:
    print(f'c = {c} continue...')
    if c == 9:
        break
    c += 1

print('*'*10)

c = 0
while c <= 9:
    print(f"c = {c} continue...")
    c += 1


#byte.py
w=b"\x74\x61\x69\x70\x65\x69"
print(w)
a=bytes.fromhex("746169706569")
print(a)
print(type(a))
bytearr = bytearray(a)
print(bytearr)
print(type(bytearr))
bytearr.pop()
print(bytearr)
bytearr.pop()
print(bytearr)
bytearr.pop()
print(bytearr)
bytearr.append(110)
print(bytearr)
bytearr.append(97)
print(bytearr)
bytearr.append(ord("n"))
print(bytearr)
