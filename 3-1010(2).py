#반복문 사용
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    molecule=1
    denominator1=1
    denominator2=1
    for j in range(M):
        molecule *= j+1
    for k in range(M-N):
        denominator1 *= k+1
    for l in range(N):
        denominator2 *= l+1        
    combination = molecule//(denominator1 * denominator2)
    print(combination)