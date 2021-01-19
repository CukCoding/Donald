import math
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    molecule = math.factorial(M)
    denominator = math.factorial(M-N) * math.factorial(N)
    combination = molecule//denominator
    print(combination)