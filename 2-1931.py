n=int(input())
meet=[]
for i in range(n):
    a,b=map(int,input().split())
    meet.append([a,b])
meet=sorted(meet, key=lambda x:x[0])
meet=sorted(meet, key=lambda x:x[1])

count = 1
for j in meet[1:]:
    if meet[0][1] <= j[0]:
        meet[0][1] = j[1]
        count+=1

print(count)