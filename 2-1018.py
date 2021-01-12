m,n=map(int, input().split())
BWarray=[]
for i in range(n):
    BWarray.append(list(map(str, input())))

black=[['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
white=[['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]

error=64
count1=0
count2=0
for a in range(m-7):
    for b in range(n-7):
        for c in range(0,8):
            for d in range(0,8):
                if BWarray[a+c][b+d]!=black[c][d]:
                    count1+=1
                if BWarray[a+c][b+d]!=white[c][d]:
                    count2+=1
        error = min(error, count1, count2)
print(error)