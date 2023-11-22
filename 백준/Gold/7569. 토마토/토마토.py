import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

tomato = list()

for _ in range(h):
    box = list()
    for _ in range(n):
        box.append(list(map(int, input().split())))
    tomato.append(box)
    
queue = deque([])

for a in range(h):
    for b in range(n):
        for c in range(m):
            if tomato[a][b][c] == 1:
                queue.append([a, b, c])
            
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]            
            
#bfs
while queue:
    z, x, y = queue.popleft()
    
    for i in range(len(dx)):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m and nz >= 0 and nz < h:
            if tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append([nz, nx, ny])
                
ans = 0

for a in tomato:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(b))

print(ans - 1)