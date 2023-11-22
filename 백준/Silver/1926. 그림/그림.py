import sys
input = sys.stdin.readline

from collections import deque

dxy = ((0, -1), (0, 1), (-1, 0), (1, 0))

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt, large = 0, 0

for r in range(n):
    for c in range(m):
        if not paper[r][c] or visited[r][c]:
            continue

        size = 0
        queue = deque([(r, c)])
        visited[r][c] = 1
        while queue:
            x, y = queue.popleft()
            size += 1

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < n or not 0 <= ny < m:
                    continue
                if not paper[nx][ny] or visited[nx][ny]:
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = 1

        cnt += 1
        large = max(large, size)

print(cnt)
print(large)