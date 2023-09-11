total = eval(input())
y = eval(input())
m = eval(input())
print(f"Month\tAmount")
for i in range(1, m + 1):
    total += total * y / 1200
    print(f"{m}\t{total:.2f}")