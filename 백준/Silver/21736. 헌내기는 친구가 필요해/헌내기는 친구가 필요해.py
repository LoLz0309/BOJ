import sys
input = sys.stdin.readline

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

xy = (-1, -1)
for i in range(n):
    if 'I' in graph[i]:
        xy = (i, graph[i].index('I'))

from collections import deque
queue = deque([xy])
graph[xy[0]][xy[1]] = 'X'

ans = 0
while queue:
    x, y = queue.popleft()

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not 0 <= nx < n or not 0 <= ny < m:
            continue
        if graph[nx][ny] == 'X':
            continue
        if graph[nx][ny] == 'P':
            ans += 1
        graph[nx][ny] = 'X'
        queue.append((nx, ny))

if ans:
    print(ans)
else:
    print('TT')