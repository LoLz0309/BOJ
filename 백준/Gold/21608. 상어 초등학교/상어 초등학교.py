import sys
input = sys.stdin.readline

DEBUG = False

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
score = (0, 1, 10, 100, 1000)

gN = 0
gClass = [[]]
gFavor = [set()]


def init() -> None:
    global gN, gClass, gFavor
    gN = int(input())
    gClass = [[0] * gN for _ in range(gN)]
    gFavor = [set() for _ in range(gN * gN + 1)]
    return


def calcSeat(s: int, x: int, y: int) -> tuple:
    fav, emp = 0, 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not 0 <= nx < gN or not 0 <= ny < gN:
            continue
        if gClass[nx][ny] == 0:
            emp += 1
        elif gClass[nx][ny] in gFavor[s]:
            fav += 1

    return fav, emp


def seatStudent(s: int) -> None:
    target = list()
    for r in range(gN):
        for c in range(gN):
            if gClass[r][c] > 0:
                continue
            fav, emp = calcSeat(s, r, c)
            target.append((fav, emp, r, c))
    target.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    gClass[target[0][2]][target[0][3]] = s
    return


def newStudent() -> None:
    args = list(map(int, input().split()))
    s = args[0]
    gFavor[s] = set(args[1:])
    seatStudent(s)
    return


def calcSatisfy(x: int, y: int) -> int:
    s = gClass[x][y]
    cnt = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not 0 <= nx < gN or not 0 <= ny < gN:
            continue
        if gClass[nx][ny] in gFavor[s]:
            cnt += 1
    return score[cnt]


def getSatisfy() -> int:
    total = 0
    for r in range(gN):
        for c in range(gN):
            total += calcSatisfy(r, c)
    return total


T = 1
for testcase in range(1, T + 1):
    init()
    for _ in range(gN * gN):
        if DEBUG:
            for c in gClass:
                print(c)
            print('----------')
        newStudent()
    print(getSatisfy())
