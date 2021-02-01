# 공유기 설치

N,C=list(map(int, input().split()))
town = []
result = 0
for i in range(N):
    town.append(int(input()))

town.sort()

first = 1
last = town[-1] - town[0]

while(first<=last):
    mid = (first + last)//2
    wifi_install = town[0]
    wifi=1
    for j in range(1,N):
        if town[j] >= wifi_install + mid:
            wifi+=1
            wifi_install = town[j]
    if wifi >= C:
        first = mid + 1
        result = mid
    else:
        last = mid -1
print(result)