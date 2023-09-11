# 209 距離判斷
# 說明:
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個點
# 的平面座標x和y值，判斷此點是否與點(5, 6)的距離
# 小於或等於15，如距離小於或等於15顯示【Inside】
# ，反之顯示【Outside】。
#
# 計算平面上兩點距離的公式：

import math

x = int(input())
y = int(input())

d = math.sqrt((x - 5) ** 2 + (y - 6) ** 2)

if d <= 15:
    print("Inside")
else:
    print("Outside")
