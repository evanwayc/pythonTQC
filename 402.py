# 402 不定數迴圈-最小值
# 說明:
# 請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值。

num=[]

while True:
    value = int(input())
    if value == 9999:
        break
    num.append(value)
print(min(num))
