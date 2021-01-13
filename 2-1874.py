n=int(input())
numberstack=[]
plusminus=[]
count=0
for i in range(n):
    num=int(input())
    while count<num:
        count+=1     
        numberstack.append(count)
        plusminus.append("+")
    if num==numberstack[-1]:
        numberstack.pop()
        plusminus.append("-")
    else:
        print("NO")
        exit()
for j in plusminus:
        print(j)