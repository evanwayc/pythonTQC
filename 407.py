while True:
    y = eval(input())
    if y == 9999: break
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("yes")
    else:
        print("no")
