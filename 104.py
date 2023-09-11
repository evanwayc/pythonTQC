# 104 圓形面積計算
# 說明:
# 請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。
#
# 需import math模組，並使用math.pi。
#
# 輸出浮點數到小數點後第二位。

import math

Radius = int(input())
Perimeter = Radius * 2 * math.pi
Area = Radius ** 2 * math.pi

print(f"Radius = {Radius:.2f}")
print(f"Perimeter = {Perimeter:.2f}")
print(f"Area = {Area:.2f}")
