# 204 算術運算
# 說明:
# 請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。

a = int(input())
b = int(input())
n = str(input())

if n == "+":
    print(a + b)
elif n == "-":
    print(a - b)
elif n == "*":
    print(a * b)
elif n == "/":
    print(a / b)
elif n == "//":
    print(a // b)
elif n == "%":
    print(a % b)
