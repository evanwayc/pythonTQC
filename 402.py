num=[]

while True:
    value = int(input())
    if value == 9999:
        break
    num.append(value)
print(min(num))
