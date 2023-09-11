n1=int(input())
n2=int(input())

sum=0


for i in range(n1,n2+1,2):
    if i%2==0:
        sum += i

print(sum)