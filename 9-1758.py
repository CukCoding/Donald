#알바생 강호

N = int(input())
money=[]
for i in range(N):
    money.append(int(input()))

money.sort(reverse=True)
TIP = 0

for i in range(1,N+1):
    if money[i-1]-(i-1) > 0:
        TIP += (money[i-1]-(i-1))
    else:
        break

print(TIP)