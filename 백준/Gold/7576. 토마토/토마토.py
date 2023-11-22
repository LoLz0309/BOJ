import sys
input = sys.stdin.readline

from collections import deque

dxy = ((0, -1), (0, 1), (-1, 0), (1, 0))

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
raw = 0
for r in range(n):
    for c in range(m):
        if tomato[r][c] == 1:
            queue.append((r, c))
        elif tomato[r][c] == 0:
            raw += 1

ans = 1

while queue:
    x, y = queue.popleft()
    ans = max(ans, tomato[x][y])

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not 0 <= nx < n or not 0 <= ny < m:
            continue
        if not tomato[nx][ny] == 0:
            continue
        queue.append((nx, ny))
        tomato[nx][ny] = tomato[x][y] + 1
        raw -= 1

if raw:
    print(-1)
else:
    print(ans - 1)
