# 406 不定數迴圈-BMI計算
# 說明:
# 請撰寫一程式，以不定數迴圈的方式輸入身高與體重，計算出BMI之後再根據以下對照表，印出BMI及相對應的BMI代表意義（State）。
# 假設此不定數迴圈輸入-9999則會結束此迴圈。
#
# 輸出浮點數到小數點後第二位。

while True:
    h = eval(input())
    if h == -9999:
        break
    h = h / 100
    w = eval(input())
    bmi = w / (h ** 2)
    print(bmi)
    if bmi < 18.5:
        print("under weight")
    elif bmi < 25:
        print("normal")
    elif bmi < 30:
        print("over weight")
    elif bmi >= 30:
        print("fat")
