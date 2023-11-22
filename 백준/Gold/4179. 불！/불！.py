import sys
input = sys.stdin.readline

from collections import deque

dxy = ((0, -1), (0, 1), (-1, 0), (1, 0))

r, c = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(r)]

jh = deque()
fire = deque()
for x in range(r):
    for y in range(c):
        if maze[x][y] == 'F':
            fire.append((x, y))
        elif not jh and maze[x][y] == 'J':
            jh.append((x, y, 1))

ans = 0
while jh:
    next_jh = deque()
    while jh:
        x, y, t = jh.popleft()
        if not maze[x][y] == 'J':
            continue
        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            ans = t
            break

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < r or not 0 <= ny < c:
                continue
            if not maze[nx][ny] == '.':
                continue
            next_jh.append((nx, ny, t + 1))
            maze[nx][ny] = 'J'
    if ans:
        break
    jh = next_jh

    next_fire = deque()
    while fire:
        x, y = fire.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < r or not 0 <= ny < c:
                continue
            if maze[nx][ny] in ('#', 'F'):
                continue
            next_fire.append((nx, ny))
            maze[nx][ny] = 'F'

    fire = next_fire

    # for mz in maze:
    #     print(*mz)
    # print()

if ans:
    print(ans)
else:
    print('IMPOSSIBLE')