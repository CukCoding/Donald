n=int(input())
number=[]
for i in range(n):
    number.insert(0,int(input()))
    number.sort()

for answer in number:
    print(answer)