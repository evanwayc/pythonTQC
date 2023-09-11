# 107 數值計算
# 說明:
# 請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。
#
# 提示：輸出浮點數到小數點後第一位。

n1 = eval(input())
n2 = eval(input())
n3 = eval(input())
n4 = eval(input())
n5 = eval(input())

print(n1, n2, n3, n4, n5)
total = n1 + n2 + n3 + n4 + n5
print(f"Sum: {total:.1f}")
avg = total / 5
print(f"Average: {avg:.1f}")
