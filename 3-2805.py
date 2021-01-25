N,M = map(int,input().split())
treehigh=list(map(int,input().split()))
first, last = 1, max(treehigh)
while first <= last:
    mid = (first+last)//2
    namu=0
    for i in treehigh:
        if i>=mid:
            namu += i - mid
    if namu >= M:
        first = mid + 1
    else:
        last = mid - 1
print(last)