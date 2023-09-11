# 109 正五邊形面積計算
# 說明:
# 請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積(Area)。
#
# 建議使用import math模組的math.pow及math.tan
#
# 正五邊形面積的公式：
#
# 輸出浮點數到小數點後第四位

import math

s = int(input())

Area = (5 * pow(s, 2)) / (4 * math.tan(math.pi / 5))

print(f"Area = {Area:.4f}")
