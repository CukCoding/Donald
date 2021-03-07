# 소수 찾기
N = int(input())
number = list(map(int, input().split()))
sosu = 0

for i in number:
    if i == 1:
        N -= 1
    for j in range(2,i):
        if i % j == 0:
            N -= 1
            break
sosu = N
print(sosu)