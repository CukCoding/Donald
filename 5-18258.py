# 큐2

import sys
from collections import deque
n = int(input())
d = deque()

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        d.append(order[1])

    elif order[0] == 'pop':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            d.popleft()
    
    elif order[0] == 'size':
        print(len(d))

    elif order[0] == 'empty':
        if len(d) != 0:
            print(0)
        else:
            print(1)
    
    elif order[0] == 'front':
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)

    elif order[0] == 'back':
        if len(d) != 0:
            print(d[-1])
        else:
            print(-1)