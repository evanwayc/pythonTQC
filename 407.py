# 407
# 不定數迴圈 - 閏年判斷
# 說明:
# 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，然後判斷它是否為閏年（leap
# year）或平年。其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。
#
# 假設此不定數迴圈輸入 - 9999
# 則會結束此迴圈。

while True:
    y = eval(input())
    if y == 9999:
        break
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("yes")
    else:
        print("no")
