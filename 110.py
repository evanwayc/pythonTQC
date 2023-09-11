# 110 正n邊形面積計算
# 說明:
# 請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。
#
# 建議使用import math模組的math.pow及math.tan
#
# 正n邊形面積的公式：
#
# 輸出浮點數到小數點後第四


import math

n = int(input())
s = int(input())

Area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(f"Area = {Area:.4f}")
