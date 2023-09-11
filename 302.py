# 302
# 迴圈偶數連加
# 說明:
# 請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），
# 利用迴圈計算從a開始的偶數連加到b的總和。例如：輸入a = 1、b = 100，則輸出結果為2550（2 + 4 + … + 100 = 2550）。

n1 = int(input())
n2 = int(input())

total = 0

for i in range(n1, n2 + 1):
    if i % 2 == 0:
        total += i

print(total)
