# 409 得票數計算
# 說明:
# 某次選舉有兩位候選人，分別是No.1: Nami、No.2:Chopper。
# 請撰寫一程式，輸入五張選票，輸入值如為1即表示針對1號候選人投票；
# 輸入值如為2即表示針對2號候選人投票，如輸入其他值則視為廢票。
# 每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；
# 如最終計算有相同的最高票數者或無法選出最高票者，顯示【=> No one wonthe election.】。
#

No1 = 0
No2 = 0
run = 1
n = 0
w = ""
while run <= 5:
    t = int(input())
    if t == 1:
        No1 += 1
    elif t == 2:
        No2 += 1
    else:
        n += 1
    print(f"Total votes for No.1 = {No1}")
    print(f"Total votes for No.2 = {No2}")
    print(f"Total null votes = {n}")
    run += 1

if No1 > No2:
    w = "No.1"
    print("No.1 won the election")
elif No2 > No1:
    w = "No.2"
    print("No.2 won the election")
