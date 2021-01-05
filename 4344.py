c=int(input())
for i in range(c):
    grade=list(map(int,input().split()))
    highperson=0
    average=sum(grade[1:])/grade[0]
    for j in grade[1:]:
        if j>average:
            highperson+=1
    print("%.3f"%round(highperson/grade[0]*100,3)+'%')