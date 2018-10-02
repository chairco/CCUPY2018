# Python 簡介


## Python 是什麼？ 

Python 是一種動態(dynamic), 直譯式(interpreted), 位元組碼編譯(bytecode-compiled)的語言。不需要對程式碼內的變數、參數、函式甚至是方法不用做任何的型態宣告。型態得確定是 Python 執行(runtime)時候才會做標註。


## Python 的歷史？

Guido van Rossum 在 1989年聖誕節無聊創造 Python 這個語言，當時 Guido 在學習 ABC 語言認為其優美且強大且適合非專業的程式設計師，不過 ABC 語言被未成功，Guido 認為是非開放，所以 Python 的發展過程被避免這個錯誤。Guido 也被被稱為 Python 之父，因為他在工作之餘也長期投入 Python 的發展(語法改進、新功能等等等)並且在關鍵時刻決定 Python 的走向也被稱為終身仁慈的獨裁者(Benevolent Dictator For Life, BDFL)，不過 2018 年 7 月 12 日在遭遇 PEP 572 事件，遭受酸民們的酸言酸語後(備註:個人認為)，他決定卸下這個職位。


## 如何開始學習 Python？

學習 Python 一種很好方法是打開 Python 的直譯器，直接鍵入代碼，例如: 你想知道增加一個 int 到 list 會發生怎樣狀況，直接使用直譯器就能快速查看結果。看看下面範例吧:

```
$ python

Python 3.6.5 (default, Jun  3 2018, 11:11:25)
[GCC 4.2.1 Compatible Clang 3.9.1 (tags/RELEASE_391/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 6
>>> a
6
>>> a + 2
8
>>> a = 'hi'
>>> len(a)
2
>>> a + len(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> a + str(a)
'hihi'
>>> a + str(len(a))
'hi2'
>>> A = 1
>>> a = 2
>>> A
1
>>> a
2
>>> foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'foo' is not defined
```

上面範例:
1. 變數可以直接賦值: 例如 a 可以再執行時隨意變成數值或是字串，另外與 Java 一樣 a, A 在 Python 是不同變數
2. 字串與數值因為不同型態，無法結合
3. 程式碼發生錯誤會觸發 error，接著拋出(raise)運作時造成中斷的錯誤訊息


## Python 哲學？

優雅、明確、簡單就是 Python 語言所倡導。Python 的開發哲學: 用一種方法，且最好是只有一種方法來做一件事(「There should be one – and preferably only one – obvious way to do it.」)。你也可以從直譯器裡 `import this` 體會 Python 哲學:

```python
import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Python 開發軟體的好處？

早期 Google 大量使用 Python 來開發軟體，原因是在不考慮效能下快速將產品實作出。因為 Python 開源精神，Python 有一個很強大的套件庫 [Pypi](https://pypi.org/) 任何人都可以使用 Python 開發自己的套件或模組，接著上傳到這個套件庫提供所有人使用，同時也可以在上面搜尋其他人貢獻的成果直接安裝套件，這樣往往可以專心著重在程式邏輯與流程進而加速開發。

Python 不同於 `C/C++/C#/Java/go/Rust/` 等這類需要編譯的程式語言，可以直接使用編譯器去驗證心裡所想的邏輯，對於非專業或是剛入門的程式設計師，能夠不需要花費太多流程與等待儘量去嘗試是棒的。


## Python 如何安裝？

如果你的電腦系統是 Windows 且正要開始學習 Python，通常我們會建議直接用 Anaconda 來安裝它，其他作業系統例如 Mac 的 OSX 或是 Linux 的 Ubuntu 等等本身則就內建 Python。不過內建的版本一般來說不會是最新，尤其是舊版本作業系統可能運作的是 Python 2.x 因此也是可以選擇使用 Anaconda 來安裝另一個新環境(不會取代內建而是共存):

[Anaconda 下載網址](https://www.anaconda.com/download/)


但如果喜歡純粹的 Python 環境，那可以到官網上直接下載安裝檔案:

[Python 下載網址](https://www.python.org/downloads/)


另外 Mac 系列的作業系統使用 [Homebrew](https://brew.sh/index_zh-tw) 這個軟體，並直接在終端機上下指令使用 `brew` 安裝


最後我們建議你使用 Python 3.x 因為 Python 2.x 已經宣布在 2020 年會停止支援，更進一步會建議至少要 3.5 以上，但 3.7 是推薦的。


## Python 內建函式

Python 的中心思想之一是「batteries included」，用來形容 Python 的內建函式庫包山包海，可以方便解決各種需求，而不需要程式設計師為了各個專案，重複建構許多常用的輔助工具。[參考](https://pycontw.kktix.cc/events/tutorial-pycon2015)

你可以從 Python 的[文件庫](https://docs.python.org/3/library/functions.html)查詢內建函式。


## Python 套件安裝(第三方函式庫)

使用 Anaconda 來安裝 Python，建議用 Anaconda 指令在終端機安裝套件的指令:

```
conda install 套件名稱
```

Python 內有個 pip 套件來安裝其他不同套件，Anaconda 底下也可以這樣安裝套件但因為 Anaconda 有自己的管理套件邏輯因此建議區隔

```
pip install 套件名稱
```


## Python 虛擬環境

通常開發過程一台電腦上不會只有一個專案，每個專案也可能會有測試的環境，因此你不會希望你所有的 Python 套件都安裝在一個環境上，因為有可能你需要不同的版本來進行測試或是因為某個原因只想使用某種版本套件。

在 Python 能夠協助你創造一個虛擬環境，虛擬環境會將套件等區隔於你的實體環境上，因此你能夠盡情的在虛擬環境上試驗不同的套件，然後刪除他也不會影響你的主要環境。

建立虛擬環境的方法很簡單:

```
$ python -m venv 你的虛擬環境名稱
```

如果使用 Anaconda 則是:
```
$ conda create -m venv python=3.7
``` 

更多請參考: https://conda.io/docs/user-guide/tasks/manage-environments.html


## Python 編輯器

適合你的編輯器可以讓開發程式更順暢，以下是我們`建議`的編輯器:

+ [vim](https://www.vim.org/)
+ [Visual Studio Code (Microsoft) ](https://code.visualstudio.com/)
+ [PyCharm (JetBrains)](https://www.jetbrains.com/pycharm/) --> 社群版免費，但進階版付費
+ [Atom (GitHub)](https://atom.io/)
+ [Sublime Text 3](https://www.sublimetext.com/)
+ [Notepad++](http://notepad-plus-plus.org/)
+ [emacs](https://www.gnu.org/software/emacs/)


通常會`反對`你使用以下工具來編輯:

+ Microsoft Word
+ Windows「記事本」
+ OS X 內建「文字編輯」
IDLE


## 最後提醒

學習程式語言都是從模仿接著用自己的想法去表達自己的概念，因此一切都是以”人“作為主體去傳達。
因此先嘗試理解，接著不斷重複的練習最後試著去改變接著內化成你的想法，是一連串不斷重複過程。

每個人理解的方法與學習的速度皆會有差異，講師的講解也可能是影響你吸收的關鍵，因此不要因課堂中跟不上而擔心難過，重要的是你已經開始想要學會這個語言，因此更多學習應該是從課堂之後開始。

當遭遇不懂，或是卡關可以加入 facebook 的 Python Taiwan 論壇或是 Ptt Python 版或是 Slack 等等群組去問問題。但不要忘記**在問問題之前你是不是已經先做過功課**，更要特別注意是問問題的**方法、禮貌與態度**，因為網路上的朋友和我一樣都是因為熱情才來指導你，讓別人感受你的尊重也才能獲得更多的幫助，對吧！更是強烈建議在問問題之前先看看這篇文章:[如何提問](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)
