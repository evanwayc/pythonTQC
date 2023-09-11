while True:
    h = eval(input())
    if h == -9999: break
    h = h/100
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
