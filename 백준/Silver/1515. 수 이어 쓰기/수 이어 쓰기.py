import sys
input = sys.stdin.readline

from collections import deque
queue = deque(list(input().rstrip()))

i = 1
while queue:
    for s in str(i):
        if queue and s == queue[0]:
            queue.popleft()
    i += 1
print(i - 1)