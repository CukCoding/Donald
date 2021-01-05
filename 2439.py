number=input()
n=int(number)
i=0
while i<=n:
    i=i+1
    print(" "*(n-i)+'*'*i)
    if i==n:
        break