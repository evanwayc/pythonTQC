# 405 不定數迴圈-分數等級
# 說明:
# 請撰寫一程式，以不定數迴圈的方式輸入一個正整數（代表分數），
# 之後根據以下分數與GPA的對照表，印出其所對應的GPA。
# 假設此不定數迴圈輸入9999則會結束此迴圈。標準如下表所示：

while True:
    n = eval(input())
    if n == 9999:
        break
    elif 90 < n < 100:
        print("A")
    elif 80 < n < 90:
        print("B")
    elif 70 < n < 80:
        print("C")
    elif 60 < n < 70:
        print("D")
    elif n < 60:
        print("E")
