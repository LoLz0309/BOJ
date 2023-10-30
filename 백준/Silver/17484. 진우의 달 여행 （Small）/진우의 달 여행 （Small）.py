import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = [[[1000] * 3 for _ in range(m)] for _ in range(n)]
ans[0] = [[graph[0][i]] * 3 for i in range(m)]

for x in range(1, n):
    for y in range(m):
        for i in range(3):
            ny = y + i - 1
            if not 0 <= ny < m:
                continue

            for j in range(3):
                if i == j:
                    continue
                ans[x][y][i] = min(ans[x][y][i], graph[x][y] + ans[x - 1][ny][j])

result = min([min(ans[-1][i]) for i in range(m)])
print(result)