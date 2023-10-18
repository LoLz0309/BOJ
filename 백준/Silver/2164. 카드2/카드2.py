import sys
from collections import deque
input = sys.stdin.readline

queue = deque([x for x in range(1, int(input()) + 1)])

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)
    
print(queue.pop())