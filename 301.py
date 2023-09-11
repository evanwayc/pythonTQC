# 301 迴圈整數連加
# 說明:
# 請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），
# 利用迴圈計算從a開始連加到b的總和。例如：輸入a=1、b=100，則輸出結果為5050（1 + 2 + … + 100 = 5050）。

n1 = int(input())
n2 = int(input())

total = 0

for i in range(n1, n2 + 1):
    total += i

print(total)
