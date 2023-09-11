# for i in range(int(input())):
#     n=str(input())
#     a = [int(j) for j in list(str(n))] # 將對應的數字轉換成數字串列，例如 11 轉換成 [1, 1]
#     print("Sum of all digits of "+str(n)+" is "+str(sum(a)))


str = input()
sum = 0
for i in str:
    sum += int(i)
print(sum)