# 108 座標距離計算
# 說明:
# 請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。
#
# 兩座標的歐式距離，輸出到小數點後第四位

import math

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

ans = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

print(f"({x1:.1f} , {y1:.1f})")
print(f"({x2:.1.} , {y2:.1f})")
print(f"Distance = {ans:.4f}")
