a=[]
b=[]
for i in range(10):
    num=int(input())
    if num%2 !=0:
        a.append(num)
    else:b.append(num)

print(f"Even numbers: {len(b)}")
print(f"Odd numbers: {len(a)}")