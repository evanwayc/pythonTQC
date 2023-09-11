# 210
# 三角形判斷
# 說明:
# 請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，檢查這三個邊長是否可以組成一個三角形。
# 若可以，則輸出該三角形之周長；否則顯示【Invalid】。
# 檢查方法 = 任意兩個邊長之總和大於第三邊長。

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print(n1 + n2 + n3)
else:
    print("Invalid")
