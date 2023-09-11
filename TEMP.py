m = eval(input())
s = eval(input())
z = eval(input())
a = (z/1.6)/(((60*m)+s)/3600)

# 速度 / 小時

print(m)
print(s)
print(z)
print(f"speed: {a:.1f}")