# 401 最小值
# 說明:
# 請撰寫一程式，由使用者輸入十個數字，然後找出其最小值，最後輸出最小值。

num = []
for i in range(10):
    num.append(input())
print(min(num))
