# 204
# 算術運算
# 說明:
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間，所有5之倍數數字總和。

n = int(input())
total = 0

for i in range(1, n + 1):
    if i % 5 == 0:
        total += i
print(total)
