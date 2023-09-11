a = int(input())
b = int(input())

num = []

for i in range(a, b + 1):
    if i % 4 == 0 or i % 9 == 0:
        num.append(i)
        print(f"{i:<4}",end="")
        if len(num) % 10 == 0:
            print()
print()
print(len(num))
print(sum(num))
