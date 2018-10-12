#-*- coding: utf-8 -*-

def fun(x, y):
    return x*y


def fun2(x, y):
    return x, y


r = fun(2, 4)
print(r)


a, b = fun2(2, 4)
print(a, b)

