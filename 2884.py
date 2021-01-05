H,M=input().split()
h=int(H)
m=int(M)
if m>=45:
    print(h,m-45)
elif m<45 and h!=0:
    print(h-1,m+15)
else:
    print(23,m+15)