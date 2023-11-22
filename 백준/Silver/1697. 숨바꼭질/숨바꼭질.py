import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

queue = deque([(n, 0)])
visited = {n}
ans = 0
while queue:
    x, t = queue.popleft()
    if x == k:
        ans = t
        break

    for nx in (x - 1, x + 1, x * 2):
        if not 0 <= nx <= 100000 or nx in visited:
            continue
        queue.append((nx, t + 1))
        visited.add(nx)

print(ans)