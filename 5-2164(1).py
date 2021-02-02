# 카드2
# 큐
n = int(input())
numberstack = list(int(i+1) for i in range(n))

while len(numberstack) > 1:
    numberstack.pop(0)
    numberstack.append(numberstack.pop(0))

for a in numberstack:
    print(a)