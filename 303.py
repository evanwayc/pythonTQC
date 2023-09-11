# 303 迴圈數值相乘
# 說明:
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數（<100），然後以三角形的方式依序輸出此數的相乘結果。

n = eval(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{j * i:<4}" , end='')
    print('')