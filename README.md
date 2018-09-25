# CCUPY2018

## 基礎 Python 課程內容

(TODO:放在投影片)
介紹講師、助教，並且介紹 Python 程式語言以及社群資源、自學資源等等。


### 帳號註冊

課程會使用 Github 與 Hankrank 讓同學可以課後自主練習，因此要先註冊這兩個帳號。

(TODO:簡單註冊教學檔案)
+ [GitHub](https://github.com/) 帳號
+ 使用 Github 帳號註冊接續註冊 [Hankrank](https://www.hackerrank.com/dashboard) 帳號


### 安裝與環境設定

建議 3.7.0 版本，但一定要 3.5 以後。

(TODO: 要有個安裝教學檔案)
科學計算或是教學：使用 Python 3.7 + Jupyter notebook 作為基礎環境＋編譯器，因此會使用 Anaconda 來安裝 Python。

(TODO: 要有個安裝教學檔案)
軟體開發角度：安裝原生 Python 3.7 + VS CODE 開發。因此會直接安裝原生 CPython。 

建立 Python 虛擬環境(Conda and 原生 Python)


### 基礎教學

(TODO: 用 Jupyter notebook 分類給學員參考的先備知識)
+ Hankrank 線上學習程式網站作為講師會講解每一個挑戰大概先備知識，接著開始試著學習。
+ 介紹 Python 的程式風格與 PEP
+ 安裝 Python 套件

#### 介紹
[Say "Hello World with Python"](https://www.hackerrank.com/challenges/py-hello-world/problem)
>簡單的 Hello World，需要先知道 print() 這個概念

[Python If-Else](https://www.hackerrank.com/challenges/py-if-else/problem)
>判斷式，在 Python 中沒有 Switch...case... 的判斷，全部以 If...Else。在範例中是以判斷奇數偶數作為挑戰，要先理解一些[運算元](https://pydoing.blogspot.com/2011/01/python-operator.html)同時也需要有些計算機概論先備知識。

[Arithmetic Operators](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem)
>運算元，需要瞭解一些資料型態 float, int

[Python: Division](https://www.hackerrank.com/challenges/python-division/problem)
>呈上，運算元除法 / 與 // 之間差異

[Loops](https://www.hackerrank.com/challenges/python-loops/problem)
>for loop, 要了解 range 概念

[Write a funcion](https://www.hackerrank.com/challenges/write-a-function/problem)
>潤年計算，較困難，可以擺在比較後面做練習。

[Print Function]()
>大概講一下 string 怎麼結合概念，然後有小技巧
        
```python
def test(x):
    return x

def run(x):
    for i in map(test, [j for j in range(1, x+1)]):
        print(i, end='')
if __name__ == '__main__':
    x = int(input())
    run(x)
```        

#### 基礎資料型態

[List Comprehernsions](https://www.hackerrank.com/challenges/list-comprehensions/problem)
>[], list() 是有速度的差異，串列表達是一層怎麼做？ data = [i for i in range(10)]

[Find the Runner-Up Score!](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)
>找次高的分數，會使用到 sort 概念可以擺後面一點
        

```python
larger, second = 0, 0
for num in arr:
    if num > larger:
        larger, second = num, larger        
    elif num == larger:
        pass
    elif num > second:
        larger, second = larger, num
```

[Nested Lists](https://www.hackerrank.com/challenges/nested-list/problem)
>需要用比較複雜的資料結構

Finding the percentage
>

Lists
>

Tuples
>

#### 字串

sWAP cASE
>

String Split and Join
>

What's Your Name?
>

Mutations
>

Find a string
>

String Validators
>

Text Alignment
>

Text Wrap
>


下面練習課後有興趣想加強自己完成

D21 Generics
>

D22 Binary Search Trees
>


### 進階應用

(TODO: 要使用 Request, Selemiun, 會用到 lxml)
開發一個爬蟲作。
    
   + PTT
   + Javascrip 的網站


### 環境管理

   + 系統內 Python 版本管理
   + 專案的管理
   + 套件的管理


## 參考資源

+ [Google Python tutorial](https://developers.google.com/edu/python/introduction)
+ [視覺顯示程式碼運作](http://www.pythontutor.com/)
+ [亮亮 - Python 初學指南](https://blog.liang2.tw/posts/2016/01/lab-coding-python/)
+ [RealPython - 豐富的線上課程](https://realpython.com/)
+ [線上手把手學習 Python](https://www.codecademy.com/learn/learn-python)
+ [爬蟲教學](https://github.com/leVirve/CrawlerTutorial)