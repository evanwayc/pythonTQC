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
