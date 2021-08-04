# 在C#內載入檔案
from init import *
from run import *

# 在C#內設定變數(object)，將python的函數(ads, inj, cas, cls)繼承過去
a, b, c, d = init()
# 將設定的變數當作參數
run(a, b, c, d)

# 這方法你試試看，我是用python來表示，我實在不想去碰C#
# 以這種方式的話，init()這個函數應該只要執行一次，剩下執行的部分都給run去跑
