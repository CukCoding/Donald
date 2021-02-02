# 카드2
# 큐
import sys
from collections import deque

n = int(input())
numberstack = deque(list(range(1,n+1)))

while len(numberstack) > 1:
    numberstack.popleft()
    numberstack.append(numberstack.popleft())

for a in numberstack:
    print(a)