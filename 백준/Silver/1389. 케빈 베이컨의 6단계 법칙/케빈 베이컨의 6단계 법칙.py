import sys
input = sys.stdin.readline

INF = 1000

n, m = map(int, input().split())
distance = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                distance[i][j] = 0
            else:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

answer = (INF * n, 0)
for i in range(1, n + 1):
    answer = min(answer, (sum(distance[i][1:]), i))
    # print(*distance[i])

print(answer[1])