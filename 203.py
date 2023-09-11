# 203 閏年判斷
# 說明:
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，然後判斷它是否為閏年（leap year）或平年。
# 其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")
