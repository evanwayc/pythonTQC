# 408
# 奇偶數個數計算
# 說明:
# 請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。

a = []
b = []
for i in range(10):
    num = int(input())
    if num % 2 != 0:
        a.append(num)
    else:
        b.append(num)

print(f"Even numbers: {len(b)}")
print(f"Odd numbers: {len(a)}")
