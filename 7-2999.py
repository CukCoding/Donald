import statistics
from sys import stdin
message = stdin.readline().strip()
N = len(message)
rc = []

for i in range(1, N+1):
    if N % i == 0:
        rc.append(i)

N_rc = len(rc)

if N_rc % 2 == 1:
    r = statistics.median(rc)
    c = statistics.median(rc)
else:
    r = statistics.median_low(rc)
    c = statistics.median_high(rc)
    


matrix = [[0 for _ in range(r)] for _ in range(c)]
for i in range(c):
    for j in range(r):
        matrix[i][j] = message[(i*r) + j]

for i in range(r):
    for j in range(c):
        print(matrix[j][i], end = "")