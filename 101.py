# 101 整數格式化輸出
# 說明: 請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、
# 欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

n1 = eval(input())
n2 = eval(input())
n3 = eval(input())
n4 = eval(input())

print(f"|{n1:>5} {n2:>5}|")
print(f"|{n3:>5} {n4:>5}|")
print(f"|{n1:<5} {n2:<5}|")
print(f"|{n3:<5} {n4:<5}|")