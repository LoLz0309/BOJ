import sys
input = sys.stdin.readline
from collections import deque

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))

gN, gM = 0, 0
gMap = [[0]]
gVisited = [[0]]

DEBUG = False
def showAll() -> None:
    print('-----------------')
    for r in range(gN):
        for c in range(gN):
            if gMap[r][c] == -2:
                print('-- ', end='')
                continue
            print(f'{gMap[r][c]:2d} ', end='')
        print()
    print('-----------------')


def init() -> None:
    global gN, gM, gMap
    gN, gM = map(int, input().split())
    gMap = [list(map(int, input().split())) for _ in range(gN)]


def searchGroup(r: int, c: int) -> tuple:
    check = gMap[r][c]
    queue = deque([(r, c)])
    gVisited[r][c] = check
    sz, rb = 1, 0
    route = list()
    while queue:
        x, y = queue.popleft()
        route.append((x, y))

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < gN or not 0 <= ny < gN:
                continue
            if gMap[nx][ny] < 0 or gVisited[nx][ny] == check:
                continue
            if gMap[nx][ny] > 0 and gMap[nx][ny] != check:
                continue
            gVisited[nx][ny] = check
            sz += 1
            if gMap[nx][ny] == 0:
                rb += 1
            queue.append((nx, ny))
    return sz, rb, route


def removeGroup(route: list) -> None:
    for x, y in route:
        gMap[x][y] = -2


def getScore() -> int:
    global gVisited
    gVisited = [[0] * gN for _ in range(gN)]

    result = list()
    for r in range(gN):
        for c in range(gN):
            if gMap[r][c] < 1 or gVisited[r][c]:
                continue
            size, rbw, rte = searchGroup(r, c)
            result.append((size, rbw, r, c, rte))
    if len(result) == 0:
        return 0
    result.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    if result[0][0] < 2:
        return 0
    removeGroup(result[0][4])
    return result[0][0] ** 2


def applyGravity() -> None:
    for c in range(gN):
        bottom = gN - 1
        for r in range(gN - 1, -1, -1):
            if gMap[r][c] == -2:
                continue
            if gMap[r][c] == -1 or r == bottom:
                bottom = r - 1
                continue
            gMap[bottom][c] = gMap[r][c]
            gMap[r][c] = -2
            bottom -= 1


def applyRotate() -> None:
    global gMap
    tmp = [[0] * gN for _ in range(gN)]
    for r in range(gN):
        for c in range(gN):
            tmp[r][c] = gMap[c][gN - r - 1]
    gMap = tmp


T = 1
for testcase in range(1, T + 1):
    init()
    if DEBUG:
        print('INIT')
        showAll()
    ans = 0
    while True:
        score = getScore()
        if score == 0:
            break
        ans += score
        if DEBUG:
            print(f'GET SCORE : {score}/{ans}')
            showAll()
        applyGravity()
        if DEBUG:
            print('APPLY GRAVITY')
            showAll()
        applyRotate()
        if DEBUG:
            print('APPLY ROTATE')
            showAll()
        applyGravity()
        if DEBUG:
            print('APPLY GRAVITY')
            showAll()
    print(ans)