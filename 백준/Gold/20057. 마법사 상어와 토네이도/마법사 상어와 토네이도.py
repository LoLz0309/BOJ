import sys
input = sys.stdin.readline

DEBUG = False
dxy = ((0, 1), (-1, 0), (0, -1), (1, 0))

gN = 0
gMap = [[]]
gTorXY = (0, 0)


def init() -> None:
    global gN, gMap, gTorXY
    gN = int(input())
    gMap = [list(map(int, input().split())) for _ in range(gN)]
    gTorXY = (gN // 2, gN // 2)


def getSandList(x, y, nx, ny, ax, ay, dx, dy, ldx, ldy, rdx, rdy) -> list:
    return  \
        [(x + ldx, y + ldy, 1), (x + rdx, y + rdy, 1),
         (nx + ldx, ny + ldy, 7), (nx + rdx, ny + rdy, 7),
         (nx + ldx * 2, ny + ldy * 2, 2), (nx + rdx * 2, ny + rdy * 2, 2),
         (ax + ldx, ay + ldy, 10), (ax + rdx, ay + rdy, 10),
         (ax + dx, ay + dy, 5)]


def blowSand(nx, ny, sand_list) -> tuple:
    out, blow = 0, 0
    for sx, sy, sp in sand_list:
        sand = (gMap[nx][ny] * sp) // 100
        blow += sand
        if not 0 <= sx < gN or not 0 <= sy < gN:
            out += sand
            continue
        gMap[sx][sy] += sand
    return out, blow


def moveTor(d: int, ld: int, rd: int) -> int:
    global gTorXY
    dx, dy = dxy[d]

    x, y = gTorXY
    nx, ny = x + dx, y + dy
    ax, ay = nx + dx, ny + dy

    sand_list = getSandList(x, y, nx, ny, ax, ay, dx, dy, *dxy[ld], *dxy[rd])
    out, blow = blowSand(nx, ny, sand_list)

    asand = gMap[nx][ny] - blow
    if 0 <= ax < gN and 0 <= ay < gN:
        gMap[ax][ay] += asand
    else:
        out += asand
    gMap[nx][ny] = 0
    gTorXY = (nx, ny)
    return out


T = 1
for testcase in range(1, T + 1):
    init()
    ans = 0
    for m2 in range(2, gN * 2 ):
        m = m2 // 2
        d = m2 % 4
        ld, rd = (d + 1) % 4, (d + 3) % 4
        for _ in range(m):
            if DEBUG:
                for mm in gMap:
                    print(mm)
                print('-------------')
            ans += moveTor(d, ld, rd)
    m = gN
    d = (gN * 2) % 4
    ld, rd = (d + 1) % 4, (d + 3) % 4
    for _ in range(m):
        if DEBUG:
            for mm in gMap:
                print(mm)
            print('-------------')
        ans += moveTor(d, ld, rd)

    print(ans)
