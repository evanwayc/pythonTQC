# 403
# 倍數總和計算
# 說明:
# 請撰寫一程式，讓使用者輸入兩個正整數a、b（a <= b），輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）以及倍數之個數、總和。
#
# 輸出欄寬為4，且需靠右對齊

a = int(input())
b = int(input())

num = []

for i in range(a, b + 1):
    if i % 4 == 0 or i % 9 == 0:
        num.append(i)
        print(f"{i:<4}", end="")
        if len(num) % 10 == 0:
            print()
print()
print(len(num))
print(sum(num))
